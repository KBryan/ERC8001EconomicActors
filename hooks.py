#!/usr/bin/env python3
"""
Multi-Agent Orchestrator Plugin - Lifecycle Hooks
Handles plugin installation, updates, and cleanup
"""

import os
import sys
import shutil


def install():
    """
    Called after plugin is placed in usr/plugins/.
    Sets up any necessary dependencies or state.
    """
    print("Installing Multi-Agent Orchestrator plugin...")
    
    # Ensure plugin tools are importable
    plugin_dir = os.path.dirname(os.path.abspath(__file__))
    if plugin_dir not in sys.path:
        sys.path.insert(0, plugin_dir)
    
    print("✅ Multi-Agent Orchestrator plugin installed successfully")
    print("   - 8 agent profiles available")
    print("   - Parallel execution tools ready")
    print("   - Use call_subordinate with profile='orchestrator' to start")
    
    return 0


def pre_update():
    """
    Called immediately before pulling new plugin code.
    Use for backup or cleanup that must happen before update.
    """
    print("Preparing for Multi-Agent Orchestrator plugin update...")
    return 0


def uninstall():
    """
    Called before plugin directory is deleted.
    Clean up any external state, dependencies, or files.
    """
    print("Uninstalling Multi-Agent Orchestrator plugin...")
    print("Note: Agent profiles in /a0/usr/agents/ are managed separately")
    print("Plugin tools and helpers will be removed")
    return 0


if __name__ == "__main__":
    # Allow manual execution for testing
    install()
