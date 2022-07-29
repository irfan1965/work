import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../auth.service';
import { Observable, Subscription } from 'rxjs';
@Component({
  selector: 'app-far',
  templateUrl: './far.component.html',
  styleUrls: ['./far.component.css']
})
export class FarComponent implements OnInit {
  [x: string]: any;



  method(): any {
    console.log(this.route.snapshot.params["id"])
    return this.route.snapshot.params["id"]
  }


  registerForm!: FormGroup;
  public imagePath: any;
  imgURL: any;
  u!: any;
  imagePreview = false

  constructor(private route: ActivatedRoute, private AuthService: AuthService, private r: Router) { }
  auth(): any {
    return this.route.snapshot.params["id"]
  }

  ngOnInit(): void {

    this.registerFormIntialization();
    if (this.auth() == 5) {
      this.registerForm.get("role")?.setValue("animal");
      let email = localStorage.getItem('email');
      this.registerForm.get('customer_email')?.setValue(email)
      console.log(email)
    }
    if (this.auth() == 4) {
      this.registerForm.get("role")?.setValue("customer");
    }
  }

  onSubmit(): any {
    // if (this.registerForm.get('role')?.value == "customer"){
    console.log(this.registerForm.get('first_name')?.value);

    const appendData = new FormData();
    appendData.append("animal_name", this.registerForm.get('animal_name')?.value),
    appendData.append("animal_age", this.registerForm.get('animal_age')?.value),
    appendData.append("animal_symptom", this.registerForm.get('animal_symptom')?.value),
    appendData.append("animal_amount", this.registerForm.get('animal_amount')?.value),
    appendData.append("animal_image", this.registerForm.get('animal_image')?.value),
    appendData.append("animal_loc", this.registerForm.get('animal_loc')?.value),
    appendData.append('role', this.registerForm.get('role')?.value),
    appendData.append('customer_email', this.registerForm.get('customer_email')?.value),


    this.AuthService.animalRegistration(appendData).subscribe(
      recData => {
        alert("registerForm Succesfull (' ')")
        this.r.navigate(['customer/customer'])

      }
    )




  }
  onFileChangeEvent(files: any) {
    var reader = new FileReader();
    this.imagePath = files;
    reader.readAsDataURL(files[0]);
    reader.onload = (_event) => {
      this.imgURL = reader.result;
      this.imagePreview = true;
    }
    this.registerForm.get('animal_image')?.patchValue(files[0]);

  }

  private registerFormIntialization() {
    this.registerForm = new FormGroup({
      'animal_name': new FormControl('', Validators.required),
      'animal_age': new FormControl('', Validators.required),
      'animal_symptom': new FormControl('', Validators.required),
      'animal_amount': new FormControl('', Validators.required),
      'animal_image': new FormControl('', Validators.required),
      'animal_loc': new FormControl('', Validators.required),
      'role': new FormControl('', Validators.required),
      'customer_email': new FormControl('', Validators.required)



    });
  }




}
