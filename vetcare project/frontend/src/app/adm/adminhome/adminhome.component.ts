import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-adminhome',
  templateUrl: './adminhome.component.html',
  styleUrls: ['./adminhome.component.css']
})
export class AdminhomeComponent implements OnInit {

  constructor(private route : Router) { }

  ngOnInit(): void {
  }
  clr() : any {
    localStorage.clear()
  }
  // role() : any {
  //   if (localStorage.getItem('role')=='customer'){
  //     return localStorage.getItem('role')
  //   }
   
  //   else if(localStorage.getItem('role')=='doctor'){
  //     console.log(localStorage.getItem('role'));
      
  //     this.route.navigate(['doctor'])

  //   }
  //   else{
  //     console.log(localStorage.getItem('role'));

  //     this.route.navigate(['admin'])

  //   }
  // }

}
