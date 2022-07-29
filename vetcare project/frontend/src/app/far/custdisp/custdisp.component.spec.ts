import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CustdispComponent } from './custdisp.component';

describe('CustdispComponent', () => {
  let component: CustdispComponent;
  let fixture: ComponentFixture<CustdispComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CustdispComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CustdispComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
