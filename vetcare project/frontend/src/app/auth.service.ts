import { Injectable, OnInit } from '@angular/core';
import { AuthComponent } from './auth/auth.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Router } from '@angular/router';
import { Token } from '@angular/compiler';

import { DatePipe } from '@angular/common';
import { CookieService } from 'ngx-cookie-service';
export const base = "http://127.0.0.1:8100/"
@Injectable({
  providedIn: 'root'
})

export class AuthService {
  userValue: any;



  chart(data : any){
return this.http.post(base+"vet/pie/",data, this.getHeaders())
  }
doctorChart(data : any){
  return this.http.post(base+"vet/doctorpie/",data, this.getHeaders()) }


adminChart(data : any){
    return this.http.post(base+"vet/adminchart/",data, this.getHeaders()) }


  getToken(){
    return localStorage.getItem('token');
  }

  isLoggged() {
    return true
  }

  getHeaders() {
    let token: any = localStorage.getItem("token");
    return {
      headers: {
        'Authorization': 'Bearer ' + token
      }
    };
  }

  constructor(private http: HttpClient, private router: Router, private cookie: CookieService) { }
  date !: any;
  d!: any;

  settings !: any;
  datetime(): any {
    this.d = new Date()
    return this.d.getMinutes()


  }
 
  animalRegistration(formData: any) {
  

    // console.log(base + 'vet/reg/')
    return this.http.post(base + 'vet/registration/', formData, this.getHeaders())


  }

  login(formData: any) {
    this.d = new Date()

    console.log(base + 'auth/');
    return this.http.post(base + 'auth/login/', formData)
  

  }
 


  userRegistration(formData: any) {
    console.log(base + 'auth/')
    return this.http.post(base + 'auth/registration/', formData, this.getHeaders())
  }
  docHistory(data: any) {
    return this.http.post(base + 'vet/doctorhistory/', data, this.getHeaders())
  }
  tok(data: any) {
    return this.http.post(base + 'auth/refresh/', data, this.getHeaders())
  }

  customerHistory(data: any): any {
    return this.http.post(base + 'vet/customerhistory/', data, this.getHeaders())
  }


  doctorInfo(data: any) {
    return this.http.post(
      base + 'auth/doctordata/', data, this.getHeaders())
  }
  doctoRequest(data: any) {
    return this.http.put(base + 'vet/doctorreq/', data, this.getHeaders())
  }

  doctorReceive(data: any) {
    return this.http.post(base + 'vet/doctorreceive/', data, this.getHeaders())
  }

  doctorUpdate(data: any) {
    return this.http.post(base + 'vet/doctorupdate/', data, this.getHeaders())
  }

  userDetails() {
    return this.http.post(base + 'auth/details/', null, this.getHeaders())
  }

  adminDoctorSearch(search: any) {
    return this.http.post(base + 'auth/adminDoctorSearch/', search, this.getHeaders())
  }

  detailsPayment() {
    return this.http.post(base + 'vet/detailspayment/', null, this.getHeaders())
  }

  adminUserDetails() {
    return this.http.post(base + 'auth/adminUserDetails/', null, this.getHeaders())
  }

  paySearch(data: any) {
    return this.http.post(base + 'vet/paysearch/', data, this.getHeaders())
  }
  adminUserSearch(data: any) {
    return this.http.post(base + 'auth/adminUserSearch/', data, this.getHeaders())

  }
  isLogged() {

  }

  refreshToken() {

    if (localStorage.getItem('token') != null) {
      console.log("refresh token function called")
      let jwtToken = JSON.parse(atob(localStorage.getItem('token')!.split('.')[1]));
      let expires = new Date(jwtToken.exp * 1000);
      let timeout = expires.getTime() - Date.now() - (60 * 1000);
      console.log("timeout " + timeout)
      setTimeout(() => {
        console.log("refreshed", localStorage.getItem('refresh'))
        this.http.post(base + 'auth/refresh/', { refresh: localStorage.getItem('refresh') }).subscribe((response: any) => {
        console.log(response, "token");
        localStorage.setItem("token", response.access);
        localStorage.setItem('refresh', response.refresh);
        this.cookie.set('acess_token', response.access);
        this.cookie.set('refresh_token', response.refresh);
        this.refreshToken();


        }
        )
      }, timeout);
    }
  }



}
// "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU3NjExMDc2LCJpYXQiOjE2NTc2MTA3NzYsImp0aSI6IjBhYTMxMzAwZmQ3ZDQxNTI5ZGU5YzNmNjI2MGUwMTU3IiwidXNlcl9pZCI6MzIsImVtYWlsIjoiZmluZUBnbWFpbC5jb20ifQ.fEVO7VXax1c88NxvDVcSAdxVE9JnAti-CL5dLfwvHr0"