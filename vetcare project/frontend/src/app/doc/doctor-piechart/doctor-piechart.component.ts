import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/auth.service';
import { Chart, registerables } from 'chart.js'


@Component({
  selector: 'app-doctor-piechart',
  templateUrl: './doctor-piechart.component.html',
  styleUrls: ['./doctor-piechart.component.css']
})
export class DoctorPiechartComponent implements OnInit {





  constructor(private AuthService: AuthService) { }
  chart: any;
  values!: any;
  datay!: any;
  user_name!: any;
  user!: any;

  ngOnInit(): void {
    this.chart = document.getElementById('myChart'),
      Chart.register(...registerables)
    this.user_name = window.localStorage.getItem('accesstoken')
    this.user = JSON.parse(this.user_name)
    var xValues = ["payments", "pendingrequest","prescription"];



    this.AuthService.doctorChart({ "email": localStorage.getItem("email") }).subscribe({
      next: (data: any) => {
        this.datay = data
        this.values = data
        console.log(data)

        console.log(this.values)
        var yValues = this.values


        var barColors = [
          "#b91d47",
          "#00aba9",
          "#2b5797",
          "#e8c3b9",

        ]

        const myChart = new Chart("myChart", {
          type: "pie",
          data: {
            labels: xValues,
            datasets: [{
              backgroundColor: barColors,
              data: yValues
            }]
          },
          options: {
            maintainAspectRatio: false,
            responsive: true,
            scales: {
              y: {
                beginAtZero: true
              }
            }
          }

        })
      }
    })
  }
}
