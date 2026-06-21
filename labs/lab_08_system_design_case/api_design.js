/*
Lab 8: API Design Stub

TODO: Implement the handler for POST /cases/:id/transition
*/

function handleTransitionRequest(req, res, database) {
  const caseId = req.params.id;
  const { newState, userId, role } = req.body;
  
  // 1. Fetch case
  // 2. Validate role permissions
  // 3. Validate state transition
  // 4. Write audit log
  // 5. Update case
  // 6. Return response
}

module.exports = { handleTransitionRequest };
