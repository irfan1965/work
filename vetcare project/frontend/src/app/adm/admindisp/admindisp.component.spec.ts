import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdmindispComponent } from './admindisp.component';

describe('AdmindispComponent', () => {
  let component: AdmindispComponent;
  let fixture: ComponentFixture<AdmindispComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AdmindispComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AdmindispComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
