#!/usr/bin/env python3
import json
import os
import sys
import subprocess
import time
from pathlib import Path
from dotenv import load_dotenv

def print_step(message):
    """Print a step message with formatting."""
    print(f"\n==> {message}")

def check_docker():
    """Check if Docker is installed and running."""
    print_step("Checking if Docker is installed and running...")
    try:
        subprocess.run(['docker', 'info'], capture_output=True, check=True)
        print("✓ Docker is ready")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ Error: Docker is not installed or not running.")
        return False

def export_discord_channel(channel_id, discord_token, output_dir):
    """Export Discord channel using DiscordChatExporter."""
    print_step(f"Exporting Discord channel {channel_id}...")
    try:
        cmd = [
            'docker', 'run', '--rm', '-i',
            '-v', f"{output_dir}:/out",
            '--env', f"DISCORD_TOKEN={discord_token}",
            'tyrrrz/discordchatexporter:stable',
            'export',
            '-f', 'Json',
            '-c', channel_id,
            '-t', discord_token
        ]
        
        result = subprocess.run(cmd, check=True, capture_output=True)
        print("✓ Successfully exported Discord channel")
        return True
    except subprocess.CalledProcessError as e:
        print("✗ Error exporting Discord channel:")
        print(f"  {e.stderr.decode()}")
        return False

def compress_conversation(conversation):
    """Create a compressed summary of conversation messages."""
    print_step("Compressing conversation...")
    summary_lines = []
    msg_count = 0
    
    for msg in conversation.get("messages", []):
        content = msg.get("content", "").strip()
        if content:
            msg_count += 1
            author = msg.get("author", {}).get("nickname", msg.get("author", {}).get("name", "Unknown"))
            timestamp = msg.get("timestamp", "").split('.')[0].replace('T', ' ')  # Format timestamp nicely
            
            # Format the message with proper indentation and line breaks
            content_lines = content.split('\n')
            if len(content_lines) > 1:
                formatted_content = '\n      '.join(content_lines)  # Indent continuation lines
                summary_lines.append(f"- {author} ({timestamp}):\n      {formatted_content}")
            else:
                summary_lines.append(f"- {author} ({timestamp}): {content}")
    
    print(f"✓ Compressed {msg_count} messages")
    return "\n\n".join(summary_lines)  # Add extra line break between messages

def get_latest_json(directory):
    """Get the most recent JSON file from the directory."""
    print_step("Looking for exported Discord data...")
    json_files = list(Path(directory).glob("*.json"))
    if not json_files:
        return None
    latest = max(json_files, key=lambda x: x.stat().st_mtime)
    print(f"✓ Found export file: {latest.name}")
    return latest

def main():
    print_step("Starting Discord conversation export and compression")
    
    # Load environment variables
    load_dotenv()
    discord_token = os.getenv('DISCORD_TOKEN')
    
    if not discord_token:
        print("✗ Error: DISCORD_TOKEN not found in .env file")
        sys.exit(1)

    # Get channel ID from command line or prompt
    if len(sys.argv) > 1:
        channel_id = sys.argv[1]
    else:
        channel_id = input("\nEnter the Discord channel ID: ").strip()
        
    if not channel_id:
        print("✗ Error: Channel ID cannot be empty")
        sys.exit(1)

    # Setup output directory
    output_dir = os.path.join(os.getcwd(), "team_chat")
    print_step(f"Setting up output directory: {output_dir}")
    os.makedirs(output_dir, exist_ok=True)
    print("✓ Output directory ready")

    # Check Docker and export channel
    if not check_docker():
        sys.exit(1)

    if not export_discord_channel(channel_id, discord_token, output_dir):
        sys.exit(1)

    # Wait briefly for the file to be written
    time.sleep(1)

    # Find and process the latest JSON file
    latest_json = get_latest_json(output_dir)
    if not latest_json:
        print("✗ No JSON files found in output directory")
        sys.exit(1)

    # Read and compress conversation
    try:
        print_step("Reading conversation data...")
        with open(latest_json, "r", encoding="utf-8") as f:
            conversation = json.load(f)
        print("✓ Successfully loaded conversation data")
        
        summary = compress_conversation(conversation)
        
        # Write compressed summary
        output_file = "team_chat.md"
        print_step(f"Writing compressed summary to {output_file}")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# Discord Channel {channel_id} - Conversation Summary\n\n")
            f.write(f"_Exported on {time.strftime('%Y-%m-%d %H:%M:%S')}_\n\n")
            f.write(summary)
        
        print(f"✓ Successfully wrote conversation summary to {output_file}")
        print("\n==> All done! 🎉")
        
    except Exception as e:
        print(f"✗ Error processing conversation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
