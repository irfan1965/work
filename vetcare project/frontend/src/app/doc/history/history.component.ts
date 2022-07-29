import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/auth.service';

@Component({
  selector: 'app-history',
  templateUrl: './history.component.html',
  styleUrls: ['./history.component.css']
})
export class HistoryComponent implements OnInit {
  docHis!:any;

  constructor(private route:Router,private http:HttpClient,private authService:AuthService) { }

  ngOnInit(): void {
    this.authService.docHistory({'doctor_email':localStorage.getItem('email')}).subscribe(
      Response => {
        console.log(Response);
        this.docHis=Response
        
      }
      )
  }
  search(event: any){
    if(event.target.player.value ){
    console.log( event.target.player.value   );
    this.authService.paySearch({'payment_id' : event.target.player.value} ).subscribe(
      Response => {
        this.docHis=Response
      }
    )

}
else{
  this.authService.docHistory({'doctor_email':localStorage.getItem('email')}).subscribe(
    Response => {
      console.log(Response);
      this.docHis=Response
      
    }
    )
}
  }


}
