import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FarComponent } from './far.component';

describe('FarComponent', () => {
  let component: FarComponent;
  let fixture: ComponentFixture<FarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FarComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
