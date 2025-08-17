from graphviz import Digraph

# Create flowchart
flowchart = Digraph(format="png")
flowchart.attr(size="6")

# Nodes
flowchart.node("Q", "❓ Wrong Commit / File Deleted")
flowchart.node("PUSH", "✅ Was it pushed to remote?")
flowchart.node("NOT_PUSHED", "Not pushed yet")
flowchart.node("RESET", "Use git reset (soft/mixed/hard)")
flowchart.node("PUSHED", "Already pushed")
flowchart.node("REVERT", "Use git revert (safe for team)")
flowchart.node("FILE", "File deleted by mistake")
flowchart.node("RESTORE", "git checkout <commit> -- file\nor git restore --source=HEAD~1 file")

# Edges
flowchart.edge("Q", "PUSH")
flowchart.edge("PUSH", "NOT_PUSHED", label="No")
flowchart.edge("NOT_PUSHED", "RESET")
flowchart.edge("PUSH", "PUSHED", label="Yes")
flowchart.edge("PUSHED", "REVERT")
flowchart.edge("Q", "FILE")
flowchart.edge("FILE", "RESTORE")

# Save & render
flowchart.render("git_conflict_resolution_flowchart", format="png")
print("✅ Flowchart generated: git_conflict_resolution_flowchart.png")
