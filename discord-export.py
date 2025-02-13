#!/usr/bin/env python3
import json
import os
import sys
import subprocess
from datetime import datetime
from dotenv import load_dotenv

def print_step(message):
    """Print a step message with timestamp."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

def check_docker():
    """Check if Docker is installed and running."""
    try:
        subprocess.run(['docker', 'info'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def export_discord_channel(channel_id, output_dir, discord_token):
    """Export Discord channel using DiscordChatExporter."""
    print_step("Exporting Discord channel...")
    
    cmd = [
        'docker', 'run', '--rm',
        '-v', f"{output_dir}:/out",
        '--env', f"DISCORD_TOKEN={discord_token}",
        'tyrrrz/discordchatexporter:stable', 'export',
        '-f', 'Json',
        '-c', channel_id,
        '-t', discord_token
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error exporting channel: {result.stderr}")
        sys.exit(1)
    
    print("✓ Channel export complete")

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
            timestamp = msg.get("timestamp", "").split('.')[0].replace('T', ' ')
            
            content_lines = content.split('\n')
            if len(content_lines) > 1:
                formatted_content = '\n      '.join(content_lines)
                summary_lines.append(f"- {author} ({timestamp}):\n      {formatted_content}")
            else:
                summary_lines.append(f"- {author} ({timestamp}): {content}")
    
    print(f"✓ Compressed {msg_count} messages")
    return "\n\n".join(summary_lines)

def main():
    # Load environment variables
    load_dotenv()
    
    # Check arguments
    if len(sys.argv) < 2:
        print("Usage: python3 script.py output_file.md [channel_id]")
        sys.exit(1)
    
    output_file = sys.argv[1]
    channel_id = sys.argv[2] if len(sys.argv) > 2 else "1332237033673850880"
    
    # Setup paths
    output_dir = os.path.join(os.getcwd(), "team_chat")
    os.makedirs(output_dir, exist_ok=True)
    
    # Get Discord token
    discord_token = os.getenv("DISCORD_TOKEN")
    if not discord_token:
        discord_token = input("Enter your Discord token: ").strip()
    
    # Check Docker
    if not check_docker():
        print("Error: Docker is not installed or not running.")
        sys.exit(1)
    
    # Export channel
    export_discord_channel(channel_id, output_dir, discord_token)
    
    # Find and process the exported JSON file
    json_files = [f for f in os.listdir(output_dir) if f.endswith('.json')]
    if not json_files:
        print("Error: No JSON files found after export")
        sys.exit(1)
    
    # Process the most recent export
    json_path = os.path.join(output_dir, json_files[0])
    with open(json_path, "r", encoding="utf-8") as f:
        conversation = json.load(f)
    
    # Create and save the summary
    summary = compress_conversation(conversation)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Compressed Conversation Summary\n\n")
        f.write(summary)
    
    print(f"✓ Summary written to {output_file}")

if __name__ == "__main__":
    main()
