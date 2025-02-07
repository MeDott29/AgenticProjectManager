# Project Task Breakdown

## Overview
This document outlines initial priorities for the project. First, we identify what Endo needs to work on, and then break those initiatives into manageable tasks for ATH.

## Tasks for Endomorphosis (endo)

1. **Project Structure & Testing Framework**
   - **Set Up Testing Environment:** Refactor the current tests into a new folder (e.g., `tests/`) with clear segregation for different hardware platforms. [Reference: endomorphosis (2025-01-31T21:49:07.306+00:00)]
   - **Define Interface Contracts:** Specify interfaces between modules (e.g., API backends, model converters, data processors). [Reference: endomorphosis (2025-01-29T05:59:24.855+00:00)]
   - **Integrate TDD:** Establish test-driven development routines; ensure every new feature module comes with unit tests. [Reference: ATH🥭 (2025-01-31T21:48:19.032+00:00)]
   
2. **API Backend & Model Server Integration**
   - **Review & Finalize API Endpoints:** Audit the endpoints defined in `ipfs_accelerate_py/api_backends/apis.py` and ensure consistency. [Reference: endomorphosis (2025-01-29T05:48:41.83+00:00)]
   - **Design the Model Server Interface:** Create clear interface definitions for how local inference, API inference, and container-based inference will interact. [Reference: endomorphosis (2025-01-28T21:39:07.898+00:00)]
   - **Prototype Model Chaining:** Define a “source-drain” mechanism for data flow among modules (e.g., for incoming audio, splitting, processing, and reassembling into text). [Reference: endomorphosis (2025-01-29T05:59:47.704+00:00)]

3. **Modular Converter & Parser Design**
   - **Establish Converter Modules:** Decide on the first set of file types to support (e.g., PDFs, PPTs, XLS) and outline the conversion pipeline. [Reference: endomorphosis (2025-01-28T21:40:45.9+00:00)]
   - **Interface for Parsers:** Draft specifications on how different parsing methods (LLM-based, non-LLM based, etc.) can be plugged-in. [Reference: endomorphosis (2025-01-28T21:42:48.8+00:00)]
   - **Implement Initial Dummy Converters:** Build simple dummy functions for each converter that can later be replaced by actual implementations. [Reference: ATH🥭 (2025-01-31T03:48:48.22+00:00)]

## Tasks for ATH

Based on the above, break down tasks into more granular work items:

1. **Testing Setup & Initial Unit Tests**
   - **File Organization:** Help in reorganizing and moving test files into a dedicated `tests/` folder. [Reference: endomorphosis (2025-01-31T21:49:07.306+00:00)]
   - **Write Sample Unit Tests:** Start by writing tests for one existing API backend (e.g., `test_api_backend.py`) to ensure the framework is working. [Reference: endomorphosis (2025-01-29T05:48:41.83+00:00)]
   - **CI/CD Integration:** Set up a simple continuous integration process (if not already in place) to run tests automatically. [Reference: endomorphosis (2025-01-29T05:48:41.83+00:00)]

2. **API Integration & Backend Support**
   - **Review and Refine API Endpoints:** Collaborate with endo in reviewing endpoints in `ipfs_accelerate_py/api_backends/apis.py` and suggest improvements. [Reference: endomorphosis (2025-01-29T05:48:41.83+00:00)]
   - **Draft Interface Documentation:** Create clear documentation (or update inline docs) for the model server and API interfaces outlining input, processing, and output formats. [Reference: endomorphosis (2025-01-29T05:59:47.704+00:00)]
   - **Prototype Data Flow:** Develop a small proof-of-concept that simulates the “source-drain” pattern for data passing through a converter. [Reference: endomorphosis (2025-01-29T06:01:49.689+00:00)]

3. **Converter & Parser Modules**
   - **Implement Dummy Converters:** Write initial dummy functions for handling a single file type (e.g., PDFs) that translate the file into text. [Reference: ATH🥭 (2025-01-29T05:52:32.885+00:00)]
   - **Document Parser Interface:** Write a short document or inline comments on how future parser integrations should work, including guidelines for TDD. [Reference: ATH🥭 (2025-01-31T21:42:48.624+00:00)]

## Next Steps
- **Discussion:** Use this document as a starting point to clarify any questions in a brief call.
- **Iteration:** Refine and modify tasks based on real-world testing and team feedback.

## Additional Tasks and References

### Additional Tasks for Endomorphosis (endo)
- **ASR/TTS/LLM Integration:** Implement asynchronous control flow to interrupt language generation when new audio is detected. [Reference: endomorphosis (2025-01-29T05:58:57.855+00:00)]
- **API & Model Server Enhancement:** Expand API backend tests and prototype model chaining for robust edge-case handling. [Reference: endomorphosis (2025-01-29T05:59:24.855+00:00)]
- **Test Automation Refinement:** Reorganize and structure tests across multiple hardware platforms as described, ensuring a solid TDD foundation. [Reference: endomorphosis (2025-01-31T21:49:07.306+00:00)]

### Additional Tasks for ATH 
- **Transformer.js Integration:** Evaluate and integrate transformer.js for model server endpoints to unify backend and client-side inference. [Reference: endomorphosis (2025-02-07T05:16:42.619+00:00)]
- **Documentation & TDD Adoption:** Update and maintain detailed interface documentation and fully adopt TDD practices for new features. [Reference: ATH🥭 (2025-01-31T21:41:54.302+00:00)]
- **CI/CD Pipeline Setup:** Collaborate to establish a robust CI/CD pipeline for automated testing and deployment.
