const bar_chart = document.getElementById('hallwaytrafficChart').getContext('2d')
new Chart(bar_chart, {
    type: "bar",
    data: {
        labels: acuity_label.map(score => 'Acuity Level ' + score),
        datasets: [{
            label: 'Stranded Patients',
            data: patient_count,
            backgroundColor: [
                '#ef4444', // Acuity 5 - Red
                '#f97316', // Acuity 4 - Orange
                '#eab308', // Acuity 3 - Yellow
                '#3b82f6', // Acuity 2 - Blue
                '#10b981'  // Acuity 1 - Green
            ],
            borderRadius: 6,
            borderWidth: 0
        }]
    }, options: {
        indexAxis: 'y',
        responsive: true,
        plugins: { legend: { display: false } },
        scales: {
            x: {
                ticks: { stepSize: 1 },
                title: { display: true, text: "Number of Stranded Patients" }
            }
        }
    }
})