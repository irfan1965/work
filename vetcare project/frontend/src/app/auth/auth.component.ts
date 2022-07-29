import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { interval } from 'rxjs';
import { AuthService } from '../auth.service';
@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css']
})
export class AuthComponent implements OnInit {
  Register!: FormGroup;
  public imagePath: any;
  imgURL: any;
  imagePreview = false
  logindata: any;
  data!: any;
  d!: any;
  constructor(private route: ActivatedRoute, private AuthService: AuthService, private r: Router) {
    if(this.AuthService.getToken()){
          if(localStorage.getItem('role')=='customer'){this.r.navigate(['customer'])}  
          else if (localStorage.getItem('role')=='doctor'){this.r.navigate(['doctor'])} 
          else{
            this.r.navigate(['admin'])
          }
        
        }
   }
  auth(): any {
    return this.route.snapshot.params["id"]
  }

  ngOnInit(): void {


    this.regDocForm();
    if (this.auth() == 2) {
      this.Register.get("role")?.setValue("doctor");
    }
    if (this.auth() == 4) {
      this.Register.get("role")?.setValue("customer");
    }
  }

  login(): any {

    const logData = new FormData();
    logData.append("email", this.Register.get('email')?.value),
      logData.append("password", this.Register.get('password')?.value)
    localStorage.setItem("email", this.Register.get('email')?.value)

    console.log(this.Register.value, "df")

    this.AuthService.login(logData).subscribe((Response: any) => {

      console.log(Response);
      if (Response == 'email'){
        alert('enter valid email')
      }
      this.data = Response
      const json = Response.email;
      setInterval(this.tok(), 10000);
      this.data = json
      console.log(Response)
      localStorage.setItem("token", Response.token)
      localStorage.setItem('refresh', Response.refresh_token)
      localStorage.setItem('token_exp', Response.token_exp)
      localStorage.setItem('role', Response.role)


      if (Response.role == 'doctor') {
        this.AuthService.refreshToken();

        this.r.navigate(['doctor'])

      }
      else if (Response.role == 'customer') {
        console.log(Response);

        this.AuthService.refreshToken();
        this.r.navigate(['customer'])

      }
      else {
        this.AuthService.refreshToken();

        this.r.navigate(['admin'])
      }

    })


  }

  tok(): any {
    this.AuthService.tok({ 'refresh': localStorage.getItem('refresh_token') })
  }
  onSubmit(): any {
    if (this.Register.get('password')?.value == this.Register.get('confirm_password')?.value) {

    }

    console.log(this.Register.get('first_name')?.value);

    const registerData = new FormData();
      registerData.append("first_name", this.Register.get('first_name')?.value),
      registerData.append("email", this.Register.get('email')?.value),
      registerData.append("password", this.Register.get('password')?.value),
      registerData.append("confirm_password", this.Register.get('confirm_password')?.value),
      registerData.append("mobile_number", this.Register.get('mobile_number')?.value),
      registerData.append("location", this.Register.get('location')?.value),
      registerData.append("doctor_exp", this.Register.get('doctor_exp')?.value),
      registerData.append("doctor_designation", this.Register.get('doctor_designation')?.value),
      registerData.append("role", this.Register.get('role')?.value),
      registerData.append("doctor_image", this.Register.get('doctor_image')?.value)

    
    localStorage.setItem("email", this.Register.get('email')?.value)

    this.AuthService.userRegistration(registerData).subscribe((Response : any) => {
      console.log(Response)
      if (Response == 'already exists') {

        alert("email already exists")
      }
     
      else {
        this.r.navigate(["auth/1"]);
        
      }




      

    }
    );


  }
  onFileChangeEvent(files: any) {
    var reader = new FileReader();
    this.imagePath = files;
    reader.readAsDataURL(files[0]);
    reader.onload = (_event) => {
      this.imgURL = reader.result;
      this.imagePreview = true;
    }
    this.Register.get('doctor_image')?.patchValue(files[0]);

  }

  private regDocForm() {
    this.Register = new FormGroup({
      'first_name': new FormControl('', Validators.required),
      'email': new FormControl('', Validators.pattern('^[a-z]*@(gmail.com|medplus.com)$')),
      'password': new FormControl('', Validators.pattern('^[a-zA-Z]*')),
      'mobile_number': new FormControl('', Validators.pattern('^[6-9][0-9]{9}$')),
      'location': new FormControl('', Validators.required),
      'confirm_password': new FormControl('', Validators.required),
      'doctor_exp': new FormControl('', Validators.required),
      'timeslot': new FormControl('', Validators.required),
      'doctor_designation': new FormControl('', Validators.required),
      'doctor_image': new FormControl('', Validators.required),
      'role': new FormControl('', Validators.required),

    });
  }
  
  onKey(event: any) {
    const inputValue = event.target.value;

    if (this.Register.get('password')?.value == inputValue) {
      console.log(inputValue, this.Register.get('password'))
    }
    else {

    }

  }


}



