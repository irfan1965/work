import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdmComponent } from './adm/adm.component';
import { AdminPiechartComponent } from './adm/admin-piechart/admin-piechart.component';
import { AdmindispComponent } from './adm/admindisp/admindisp.component';
import { AdminhomeComponent } from './adm/adminhome/adminhome.component';
import { DetailsComponent } from './adm/details/details.component';
import { UserComponent } from './adm/user/user.component';
import { AuthComponent } from './auth/auth.component';
import { AuthenticationGuard } from './authentication.guard';
import { BaseComponent } from './base/base.component';
import { DocComponent } from './doc/doc.component';
import { DochomeComponent } from './doc/dochome/dochome.component';
import { DoctorPiechartComponent } from './doc/doctor-piechart/doctor-piechart.component';
import { HistoryComponent } from './doc/history/history.component';
import { ReqComponent } from './doc/req/req.component';
import { CustHisComponent } from './far/cust-his/cust-his.component';
import { CustdispComponent } from './far/custdisp/custdisp.component';
import { DispComponent } from './far/disp/disp.component';
import { FarComponent } from './far/far.component';
import { HomeComponent } from './far/home/home.component';
import { PiechartComponent } from './far/piechart/piechart.component';
import { WrongroutingComponent } from './wrongrouting/wrongrouting.component';
 const routes: Routes = [
  {path:"",component:BaseComponent},
  
  {path:"auth/:id",component:AuthComponent},
  {path:"admin",component:AdminhomeComponent,
  children : [
        {path:"",component:AdmComponent,canActivate : [AuthenticationGuard]},
        {path:"home",component:AdmComponent,canActivate : [AuthenticationGuard]},
        {path:"doctor",component:AdmindispComponent,canActivate : [AuthenticationGuard]},
        {path:"payment",component:DetailsComponent,canActivate : [AuthenticationGuard]},
        {path:"user",component:UserComponent,canActivate : [AuthenticationGuard]},
        {path:"adminpie",component:AdminPiechartComponent},

        
  ]
},


  {path:"doctorregisteration/:id",component:AuthComponent},
  {path:"customerregistration/:id",component:AuthComponent},

  {path:"customer",component:HomeComponent,canActivate : [AuthenticationGuard],
  children:[    
    {path:'',component:CustdispComponent,canActivate : [AuthenticationGuard] },
    {path:'homepage',component:CustdispComponent,  canActivate : [AuthenticationGuard]},
    {path : "customer",component:DispComponent,  canActivate : [AuthenticationGuard]},
    { path : 'book/:id', component:FarComponent,  canActivate : [AuthenticationGuard] },
    { path : 'history/:id', component:CustHisComponent ,  canActivate : [AuthenticationGuard] },
    { path : 'log/:id', component:FarComponent ,  canActivate : [AuthenticationGuard]},
  {path : 'statistics', component:PiechartComponent ,  canActivate : [AuthenticationGuard]},
  


  // adminpie
  ]

  },

  { path:'doctor',component:DochomeComponent  ,  canActivate : [AuthenticationGuard],
children:[
        {path:"",component:DocComponent ,  canActivate : [AuthenticationGuard]},
        {path:'homepage',component:DocComponent ,  canActivate : [AuthenticationGuard]},
        {path:"request",component:ReqComponent ,  canActivate : [AuthenticationGuard]},
        {path:"doctorhistory",component:HistoryComponent ,  canActivate : [AuthenticationGuard]} ,
      {path:'Statistics',component:DoctorPiechartComponent ,  canActivate : [AuthenticationGuard]} ]

},
{ path: '**', component:WrongroutingComponent }


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
