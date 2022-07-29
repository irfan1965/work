import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-wrongrouting',
  templateUrl: './wrongrouting.component.html',
  styleUrls: ['./wrongrouting.component.css']
})
export class WrongroutingComponent implements OnInit {

  constructor(private route :Router) { }

  ngOnInit(): void {
    if(localStorage.getItem('role')=='doctor'){
      this.route.navigate(['doctor'])
    }
    else   if(localStorage.getItem('role')=='customer'){
      this.route.navigate(['customer'])
    }
    else {
      this.route.navigate(['admin'])
    }
  }
 

}
