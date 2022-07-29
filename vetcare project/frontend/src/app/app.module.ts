import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BaseComponent } from './base/base.component';
import { DocComponent } from './doc/doc.component';
import { FarComponent } from './far/far.component';
import { AdmComponent } from './adm/adm.component';
import { AuthComponent } from './auth/auth.component';
import { FormsModule,ReactiveFormsModule,FormControl,FormGroup } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { DispComponent } from './far/disp/disp.component';
import { HomeComponent } from './far/home/home.component';
import { DochomeComponent } from './doc/dochome/dochome.component';
import { HistoryComponent } from './doc/history/history.component';
import { ReqComponent } from './doc/req/req.component';
import { CustHisComponent } from './far/cust-his/cust-his.component';
import { CustdispComponent } from './far/custdisp/custdisp.component';
import { AdmindispComponent } from './adm/admindisp/admindisp.component';
import { AdminhomeComponent } from './adm/adminhome/adminhome.component';
import { DetailsComponent } from './adm/details/details.component';
import { UserComponent } from './adm/user/user.component';
import { DatePipe } from '@angular/common';
import { AuthService } from './auth.service';
import { CookieService } from 'ngx-cookie-service';
import { ChartComponent, NgApexchartsModule } from 'ng-apexcharts';
import { PiechartComponent } from './far/piechart/piechart.component';
import { NgChartsModule } from 'ng2-charts';
import { DoctorPiechartComponent } from './doc/doctor-piechart/doctor-piechart.component';
import { WrongroutingComponent } from './wrongrouting/wrongrouting.component';
import { AdminPiechartComponent } from './adm/admin-piechart/admin-piechart.component';
@NgModule({
  declarations: [
    AppComponent,
    BaseComponent,
    DocComponent,
    FarComponent,
    AdmComponent,
    AuthComponent,
    DispComponent,
    HomeComponent,
    DochomeComponent,
    HistoryComponent,
    ReqComponent,
    CustHisComponent,
    CustdispComponent,
    AdmindispComponent,
    AdminhomeComponent,
    DetailsComponent,
    UserComponent,
    PiechartComponent,
    DoctorPiechartComponent,
    WrongroutingComponent,
    AdminPiechartComponent,
    
    
  
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    // HttpClient,
    HttpClientModule,
    NgApexchartsModule,
    NgChartsModule,
    


    
    
  ],
  providers: [AuthService,CookieService],
  bootstrap: [AppComponent]
})
export class AppModule { }
