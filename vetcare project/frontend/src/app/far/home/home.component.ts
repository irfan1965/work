import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private cookie :CookieService ,private  route :Router) { }

  ngOnInit(): void {
  }
  local():any{
    localStorage.clear()
    this.cookie.deleteAll()
  }
  role() : any {
    if (localStorage.getItem('role')=='customer'){
      return localStorage.getItem('role')
    }
   
    else if(localStorage.getItem('role')=='doctor'){
      console.log(localStorage.getItem('role'));
      
      this.route.navigate(['doctor'])

    }
    else{
      console.log(localStorage.getItem('role'));

      this.route.navigate(['admin'])

    }
  }

}
