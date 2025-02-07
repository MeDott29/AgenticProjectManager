# Project Task Breakdown

## Overview
This document outlines initial priorities for the project. First, we identify what Endo needs to work on, and then break those initiatives into manageable tasks for ATH.

## Tasks for Endomorphosis (endo)

1. **Project Structure & Testing Framework**
   - **Set Up Testing Environment:** Refactor the current tests into a new folder (e.g., `tests/`) with clear segregation for different hardware platforms.
   - **Define Interface Contracts:** Specify interfaces between modules (e.g., API backends, model converters, data processors).
   - **Integrate TDD:** Establish test-driven development routines; ensure every new feature module comes with unit tests.
   
2. **API Backend & Model Server Integration**
   - **Review & Finalize API Endpoints:** Audit the endpoints defined in `ipfs_accelerate_py/api_backends/apis.py` and ensure consistency.
   - **Design the Model Server Interface:** Create clear interface definitions for how local inference, API inference, and container-based inference will interact.
   - **Prototype Model Chaining:** Define a “source-drain” mechanism for data flow among modules (e.g., for incoming audio, splitting, processing, and reassembling into text).

3. **Modular Converter & Parser Design**
   - **Establish Converter Modules:** Decide on the first set of file types to support (e.g., PDFs, PPTs, XLS) and outline the conversion pipeline.
   - **Interface for Parsers:** Draft specifications on how different parsing methods (LLM-based, non-LLM based, etc.) can be plugged-in.
   - **Implement Initial Dummy Converters:** Build simple dummy functions for each converter that can later be replaced by actual implementations.

## Tasks for ATH

Based on the above, break down tasks into more granular work items:

1. **Testing Setup & Initial Unit Tests**
   - **File Organization:** Help in reorganizing and moving test files into a dedicated `tests/` folder.
   - **Write Sample Unit Tests:** Start by writing tests for one existing API backend (e.g., `test_api_backend.py`) to ensure the framework is working.
   - **CI/CD Integration:** Set up a simple continuous integration process (if not already in place) to run tests automatically.

2. **API Integration & Backend Support**
   - **Review and Refine API Endpoints:** Collaborate with endo in reviewing endpoints in `ipfs_accelerate_py/api_backends/apis.py` and suggest improvements.
   - **Draft Interface Documentation:** Create clear documentation (or update inline docs) for the model server and API interfaces outlining input, processing, and output formats.
   - **Prototype Data Flow:** Develop a small proof-of-concept that simulates the “source-drain” pattern for data passing through a converter.

3. **Converter & Parser Modules**
   - **Implement Dummy Converters:** Write initial dummy functions for handling a single file type (e.g., PDFs) that translate the file into text.
   - **Document Parser Interface:** Write a short document or inline comments on how future parser integrations should work, including guidelines for TDD.

## Next Steps
- **Discussion:** Use this document as a starting point to clarify any questions in a brief call.
- **Iteration:** Refine and modify tasks based on real-world testing and team feedback.
