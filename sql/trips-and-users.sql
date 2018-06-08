# Write your MySQL query statement below

# Install MySQL via Docker
# https://hub.docker.com/r/mysql/mysql-server/

SELECT Trips.Request_at AS Day, ROUND(COUNT(CASE WHEN Trips.Status IN ('cancelled_by_client', 'cancelled_by_driver') THEN Trips.Status END)/COUNT(*), 2) AS "Cancellation Rate" FROM Trips INNER JOIN Users ON Trips.Client_Id=Users.Users_Id WHERE Users.Banned='No' AND Trips.Request_at>='2013-10-01' AND Trips.Request_at<='2013-10-03' GROUP BY Trips.Request_at
