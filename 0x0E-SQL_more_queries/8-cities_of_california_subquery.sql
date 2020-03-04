-- California Cities
a = (SELECT id from states WHERE name="California");
SELECT id from cities WHERE state_id=a;
