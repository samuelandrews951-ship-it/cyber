<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Real-Time Cyber Attack Map</title>

    <!-- Leaflet Map CDN -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #0f172a;
            color: white;
            text-align: center;
        }

        h1 {
            margin: 15px;
        }

        #map {
            height: 450px;
            width: 90%;
            margin: auto;
            border-radius: 10px;
        }

        table {
            margin: 20px auto;
            border-collapse: collapse;
            width: 80%;
        }

        th, td {
            border: 1px solid #38bdf8;
            padding: 10px;
        }

        th {
            background-color: #0284c7;
        }
    </style>
</head>
<body>

<h1>🌐 Real-Time Cyber Attack Map</h1>
<p>Simulated global cyber attack visualization (CRT Demo)</p>

<div id="map"></div>

<table>
    <tr>
        <th>Time</th>
        <th>Attack Type</th>
        <th>Country</th>
        <th>Severity</th>
    </tr>
    <tbody id="attackTable"></tbody>
</table>

<script>
    // Initialize map
    var map = L.map('map').setView([20, 0], 2);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data © OpenStreetMap'
    }).addTo(map);

    // Sample attack data
    var attacks = [
        {time: "10:30:15", type: "DDoS", country: "India", lat: 20.59, lon: 78.96, severity: "High"},
        {time: "10:32:40", type: "Phishing", country: "USA", lat: 37.09, lon: -95.71, severity: "Medium"},
        {time: "10:35:10", type: "Malware", country: "Germany", lat: 51.16, lon: 10.45, severity: "Critical"}
    ];

    // Plot attacks
    attacks.forEach(a => {
        L.circleMarker([a.lat, a.lon], {
            radius: 8,
            color: "red"
        }).addTo(map)
        .bindPopup(
            "Attack: " + a.type +
            "<br>Country: " + a.country +
            "<br>Severity: " + a.severity
        );

        document.getElementById("attackTable").innerHTML +=
            `<tr>
                <td>${a.time}</td>
                <td>${a.type}</td>
                <td>${a.country}</td>
                <td>${a.severity}</td>
            </tr>`;
    });
</script>

</body>
</html>
