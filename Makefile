.PHONY: build clean fmt help install lint lock publish test
.DEFAULT_GOAL := help

UV ?= uv

define PRINT_HELP
awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_.-]+:.*?## / {printf "%-16s %s\n", $$1, $$2}' $(MAKEFILE_LIST)
endef

help: ## Show available make targets.
	@$(PRINT_HELP)

install: ## Create or update the local development environment with uv.
	$(UV) sync --dev

lock: ## Refresh the dependency lockfile with uv.
	$(UV) lock --update

lint: ## Run static analysis checks.
	$(UV) run ruff check .

fmt: ## Format the codebase.
	$(UV) run ruff format .

test: ## Execute the test suite.
	$(UV) run pytest

build: ## Build source and wheel distributions.
	$(UV) build

publish: ## Publish the package to the configured index.
	$(UV) publish

clean: ## Remove build artifacts and caches.
	rm -rf .ruff_cache .pytest_cache build dist *.egg-info
