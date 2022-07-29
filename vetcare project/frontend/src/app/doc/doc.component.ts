import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-doc',
  templateUrl: './doc.component.html',
  styleUrls: ['./doc.component.css']
})
export class DocComponent implements OnInit {

  constructor(private router:ActivatedRoute) { }

  ngOnInit(): void {

  }
  value():any{
    return this.router.snapshot.params["id"]
  }

}
