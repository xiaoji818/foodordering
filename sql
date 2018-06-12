SELECT sensor_id, COUNT(DISTINCT event_type) AS TYPES FROM events
GROUP BY sensor_id
ORDER BY sensor_id ASC;

SELECT a.event_type,(a.value-b.value) AS value FROM
events as a JOIN 
events as b 
ON 
a.event_type = b.event_type
AND
a.time = (SELECT time FROM events AS event1 
          WHERE event1.event_type=a.event_type 
          ORDER BY time DESC LIMIT 1)
AND 
b.time = (SELECT time FROM events AS event2 
          WHERE event2.event_type=b.event_type
          ORDER BY time DESC LIMIT 1 OFFSET 1)
;

/*In Customer Case 6 and 7, the code does not work when two event_type have the same time stamp.*/