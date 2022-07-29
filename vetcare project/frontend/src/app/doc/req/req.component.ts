import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/auth.service';
import { FormControlName } from '@angular/forms';

@Component({
  selector: 'app-req',
  templateUrl: './req.component.html',
  styleUrls: ['./req.component.css']
})
export class ReqComponent implements OnInit {
  data!:any;
  prescriptions!:any;
  a!:any;

  constructor(private router:Router,private http:HttpClient,private authService:AuthService) { }

  ngOnInit(): void {
    this.getDoctorData();
  }
  
  cur(data:any):any{
    console.log(data, 'pres:' +this.a);
 
    this.authService.doctorUpdate({'email':localStorage.getItem('email'),data,'details_prescription':this.a}).subscribe(response => {
      this.prescriptions = response
      this.getDoctorData();
    })
  }

  getDoctorData() {   
    this.authService.doctorReceive({'email':localStorage.getItem('email')}).subscribe(response => {
      this.prescriptions = response
    })
  }

prescription(event:any)
{
this.a=(event.target as HTMLInputElement).value;
console.log(this.a);


}
}