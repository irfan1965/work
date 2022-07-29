import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CustHisComponent } from './cust-his.component';

describe('CustHisComponent', () => {
  let component: CustHisComponent;
  let fixture: ComponentFixture<CustHisComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CustHisComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CustHisComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
