const assert = require('assert');
const { isValidTransition } = require('./state_machine');

// Test 1: Analyst can move OPEN to IN_PROGRESS
assert.strictEqual(isValidTransition("OPEN", "IN_PROGRESS", "ANALYST"), true);

// Test 2: Analyst CANNOT move PENDING_APPROVAL to CLOSED
assert.strictEqual(isValidTransition("PENDING_APPROVAL", "CLOSED", "ANALYST"), false);

// Test 3: Supervisor CAN move PENDING_APPROVAL to CLOSED
assert.strictEqual(isValidTransition("PENDING_APPROVAL", "CLOSED", "SUPERVISOR"), true);

console.log("All tests passed (if implemented correctly)!");
