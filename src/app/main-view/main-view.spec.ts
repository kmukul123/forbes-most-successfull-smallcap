import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';

import { MainView } from './main-view';

describe('MainView', () => {
  let component: MainView;
  let fixture: ComponentFixture<MainView>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MainView, HttpClientTestingModule]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MainView);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
