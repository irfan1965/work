import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/auth.service';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {
  details !: any;
  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    this.authService.adminUserDetails().subscribe(
      Response => {
        this.details = Response
        console.log(this.details);

      }
    )
  }
  search(event: any) {
    if (event.target.player.value) {
      console.log(event.target.player.value,"sdkj");
      this.authService.adminUserSearch({ 'search': event.target.player.value }).subscribe(
        Response => {
          this.details = Response
          console.log(this.details);


        }
      )

    }
    else {
      this.authService.adminUserDetails().subscribe(
        Response => {
          this.details = Response
          console.log(this.details,"empty");

        }
      )
    }
  }


}

