def detect_discharge_blockers(patients, tasks):
    # Group pending tasks by patient
    pending_tasks = {}
    for t in tasks:
        if t["status"] == "pending":
            pid = t["patient_id"]
            if pid not in pending_tasks:
                pending_tasks[pid] = []
            pending_tasks[pid].append(t)
            
    results = []
    for p in patients:
        if p["status"] == "medically_ready":
            pid = p["id"]
            if pid in pending_tasks:
                # Pick the first pending task as the primary blocker for simplicity
                primary = pending_tasks[pid][0]
                results.append({
                    "patient_id": pid,
                    "blocker": primary["type"],
                    "owner": primary["owner"],
                    "total_pending": len(pending_tasks[pid])
                })
                
    return results
