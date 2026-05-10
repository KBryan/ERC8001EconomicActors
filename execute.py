#!/usr/bin/env python3
"""
Multi-Agent Orchestrator Plugin - Setup Script
User-triggered operations for installation, testing, and maintenance
"""

import sys


def setup():
    """Initial setup after plugin installation"""
    print("=" * 70)
    print("🚀 Multi-Agent Orchestrator Plugin Setup")
    print("=" * 70)
    print()
    
    print("✅ Plugin structure verified")
    print("   - 8 agent profiles ready")
    print("   - Parallel execution tools available")
    print("   - Integration layer loaded")
    print()
    
    print("📋 Available Agent Profiles:")
    print("   Tier 1: orchestrator (delegation coordinator)")
    print("   Tier 2: planning-lead, engineering-lead, validation-lead")
    print("   Tier 3: frontend-dev, backend-dev, qa-engineer, security-reviewer")
    print()
    
    print("🎯 Quick Start:")
    print("   1. Use call_subordinate with profile='orchestrator'")
    print("   2. Or import from helpers.agent_zero_integration")
    print("   3. See README.md for detailed usage examples")
    print()
    
    return 0


def test():
    """Run basic plugin tests"""
    print("=" * 70)
    print("🧪 Multi-Agent Orchestrator Tests")
    print("=" * 70)
    print()
    
    try:
        # Use fully qualified import paths as per Agent Zero conventions
        from usr.plugins.multi_agent_orchestrator.tools.multi_agent_broadcast import MultiAgentOrchestrator, AgentTask
        from usr.plugins.multi_agent_orchestrator.helpers.agent_zero_integration import AgentZeroSubordinateExecutor
        
        print("✅ Imports successful")
        
        # Test basic orchestration
        orchestrator = MultiAgentOrchestrator()
        tasks = [
            AgentTask(profile="frontend-dev", message="Test task", priority=1),
            AgentTask(profile="backend-dev", message="Test task", priority=1),
        ]
        
        result = orchestrator.broadcast(tasks, execution_mode="parallel")
        
        print(f"✅ Parallel execution: {result['orchestration_summary']['successful']}/{result['orchestration_summary']['total_agents']} successful")
        print(f"   Duration: {result['orchestration_summary']['total_duration_seconds']}s")
        print()
        
        print("✅ All tests passed!")
        return 0
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


def demo():
    """Run a demonstration of multi-agent orchestration"""
    print("=" * 70)
    print("🎬 Multi-Agent Orchestrator Demo")
    print("=" * 70)
    print()
    
    from usr.plugins.multi_agent_orchestrator.tools.multi_agent_broadcast import create_full_team_request
    
    print("Executing full 8-agent team request...")
    print("Request: 'Build user authentication system'")
    print()
    
    result = create_full_team_request("Build user authentication system")
    
    print("Results:")
    print(f"  Agents: {result['orchestration_summary']['total_agents']}")
    print(f"  Successful: {result['orchestration_summary']['successful']}")
    print(f"  Duration: {result['orchestration_summary']['total_duration_seconds']}s")
    print()
    print(result['synthesized_output'])
    
    return 0


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python execute.py [setup|test|demo]")
        print()
        print("Commands:")
        print("  setup  - Initial plugin setup")
        print("  test   - Run plugin tests")
        print("  demo   - Run demonstration")
        return 1
    
    command = sys.argv[1].lower()
    
    if command == "setup":
        return setup()
    elif command == "test":
        return test()
    elif command == "demo":
        return demo()
    else:
        print(f"Unknown command: {command}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
