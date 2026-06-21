const VALID_TRANSITIONS = {
  "OPEN": {
    "IN_PROGRESS": ["ANALYST", "SUPERVISOR"]
  },
  "IN_PROGRESS": {
    "PENDING_APPROVAL": ["ANALYST", "SUPERVISOR"]
  },
  "PENDING_APPROVAL": {
    "CLOSED": ["SUPERVISOR"],
    "IN_PROGRESS": ["SUPERVISOR"]
  }
};

function isValidTransition(currentState, newState, role) {
  if (!VALID_TRANSITIONS[currentState]) return false;
  
  const allowedRoles = VALID_TRANSITIONS[currentState][newState];
  if (!allowedRoles) return false;
  
  return allowedRoles.includes(role);
}

function handleTransitionRequest(req, res, database) {
  // Mock implementation
  const { currentState } = database.getCase(req.params.id);
  
  if (!isValidTransition(currentState, req.body.newState, req.body.role)) {
    return res.status(403).json({ error: "Invalid transition or permission denied" });
  }
  
  database.transaction(() => {
    database.updateCaseState(req.params.id, req.body.newState);
    database.writeAuditLog({ caseId: req.params.id, action: req.body.newState, user: req.body.userId });
  });
  
  return res.status(200).json({ success: true });
}

module.exports = { isValidTransition, handleTransitionRequest };
