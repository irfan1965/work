import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/auth.service';

@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.css']
})
export class DetailsComponent implements OnInit {
details!:any;
  constructor(private authService:AuthService) { }

  ngOnInit(): void {

    this.authService.detailsPayment().subscribe(
      Response => {
        this.details =Response
        console.log(this.details);
        
      }
    )
  }
  search(event: any) {
    if (event.target.player.value) {
      console.log(event.target.player.value,"sdkj");
      this.authService.paySearch({ 'payment_id': event.target.player.value }).subscribe(
        Response => {
          this.details = Response
        }
      )

    }
    else {
      
    this.authService.detailsPayment().subscribe(
      Response => {
        this.details =Response
        console.log(this.details);
        
      }
    )
    }
  }
}
