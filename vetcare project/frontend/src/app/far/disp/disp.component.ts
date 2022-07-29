import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/auth.service';
@Component({
  selector: 'app-disp',
  templateUrl: './disp.component.html',
  styleUrls: ['./disp.component.css']
})

export class DispComponent implements OnInit {
  data!:any;
  u!:any;

  constructor(private router:Router,private AuthService:AuthService) { }

  ngOnInit(): void {
    this.AuthService.doctorInfo(this.data).subscribe(
      Response=>{
        this.u=Response
        console.log(this.u,localStorage.getItem('email'),"yufr")
      })
  }
  docreq(email:any):any{
    this.AuthService.doctoRequest({doctor_email:email,customer_email:localStorage.getItem('email')}).subscribe(
      Response=>{
        this.u=Response
        console.log(this.u,"yuf")
      })
      this.router.navigate(['customer'])

  }

}
