import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router, TitleStrategy } from '@angular/router';
import { AuthService } from 'src/app/auth.service';
@Component({
  selector: 'app-cust-his',
  templateUrl: './cust-his.component.html',
  styleUrls: ['./cust-his.component.css']
})
export class CustHisComponent implements OnInit {
  data!:any;
  custinfo!:any;
  srch!:any;
  value!:any;
  constructor(private route:Router,private http:HttpClient, private auth:AuthService,private router:ActivatedRoute) { }

  ngOnInit(): void {

      this.auth.customerHistory({'customer_email':localStorage.getItem('email')}).subscribe( (Response: any) => {
        this.custinfo=Response
        console.log(Response);})
  
  }
  search(event: any){
    if  (event.target.player.value){
    console.log( event.target.player.value  );
    this.auth.paySearch({'payment_id' : event.target.player.value} ).subscribe(
      Response => {
        this.custinfo=Response
      }
    )
    
  }
  else{
    console.log("hi");
    this.auth.customerHistory({'customer_email':localStorage.getItem('email')}).subscribe( (Response: any) => {
      this.custinfo=Response
      console.log(Response);})
    
    
  }
}

}
