import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/auth.service';

@Component({
  selector: 'app-admindisp',
  templateUrl: './admindisp.component.html',
  styleUrls: ['./admindisp.component.css']
})
export class AdmindispComponent implements OnInit {
  user!: any;

  constructor(private route:Router,private authservice:AuthService) { }

  ngOnInit(): void {
    this.authservice.userDetails().subscribe(
      Response => {
        this.user=Response
        console.log(Response);
        
      }
      )
  }
  // userdetails() : any {}
  search(event: any) {
    if (event.target.player.value) {
      console.log(event.target.player.value,"sdkj");
      this.authservice.adminDoctorSearch({ 'search': event.target.player.value }).subscribe(
        Response => {
          this.user = Response
          console.log(this.user);


        }
      )

    }
    else {
      this.authservice.userDetails().subscribe(
        Response => {
          this.user=Response
          console.log(Response);
          
        }
        )
    }
  }

}
