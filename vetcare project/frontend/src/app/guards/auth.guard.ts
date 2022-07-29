import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';


@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(private authService :AuthService,private  router : Router) { }
  canActivate(){
    if (this.authService.isLoggged()){
      this.router.navigate(['/srcret-random-number'])
    }
    return !this.newMethod();
  }

  private newMethod():any {
    return this.authService.isLogged();
  }
    }
