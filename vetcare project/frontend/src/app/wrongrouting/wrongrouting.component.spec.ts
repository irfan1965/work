import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WrongroutingComponent } from './wrongrouting.component';

describe('WrongroutingComponent', () => {
  let component: WrongroutingComponent;
  let fixture: ComponentFixture<WrongroutingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WrongroutingComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WrongroutingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
