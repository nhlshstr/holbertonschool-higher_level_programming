-- California Cities
SELECT id, name from cities WHERE state_id = (SELECT id from states WHERE name = "California");
