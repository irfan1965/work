import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DoctorPiechartComponent } from './doctor-piechart.component';

describe('DoctorPiechartComponent', () => {
  let component: DoctorPiechartComponent;
  let fixture: ComponentFixture<DoctorPiechartComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DoctorPiechartComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DoctorPiechartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
