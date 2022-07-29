import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-dochome',
  templateUrl: './dochome.component.html',
  styleUrls: ['./dochome.component.css']
})
export class DochomeComponent implements OnInit {
 

  constructor(private cookie : CookieService,private route:Router) { }

  ngOnInit(): void {
  }
  role() : any{
    if (localStorage.getItem('role')=='doctor'){
      console.log(localStorage.getItem('role'),"sdj");
      
    return localStorage.getItem('role')}
    
    else if(localStorage.getItem('role')=='customer'){
      this.route.navigate(['customer'])

    }
    else{
      this.route.navigate(['admin'])

    }


  }

  local():any{
    localStorage.clear()
    this.cookie.deleteAll()
  }
}
