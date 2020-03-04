-- California Cities
a = (SELECT id from states WHERE name="California");
SELECT id, name from cities WHERE state_id=a;
