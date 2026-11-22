import { Component, OnInit } from '@angular/core';
import { Room } from '../room';
import { GenericService } from '../generic';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-rooms-filter',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './rooms-filter.html',
  styleUrl: './rooms-filter.css',
})
export class RoomsFilter implements OnInit {

  selectedFilter: string = 'nbBeds';
  selectedOption: string = '';

  nbBedsList: number[] = [];
  categories: string[] = [];
  prices: number[] = [];
  filteredRooms: Room[] = [];
  paginatedRooms: Room[] = [];

  currentPage: number = 1;
  pageSize: number = 4;

  constructor(private genericService: GenericService, private cdr:ChangeDetectorRef) {}

  ngOnInit(): void {
    this.getNbBeds();
    this.getCategories();
    this.getPrices();
    this.fetchAllRooms();
  }

  fetchAllRooms(): void {
  this.genericService.fetchRooms().subscribe((rooms: Room[]) => {
    this.filteredRooms = rooms;
    this.updatePagination();
    this.cdr.detectChanges();
  });
}

  onFilterChange(): void {
    this.selectedOption = '';
    this.filteredRooms = [];
    this.currentPage = 1;
  }

applyFilter(): void {
  this.currentPage = 1;

  if (!this.selectedOption) {
    this.fetchAllRooms();
    return;
  }

  const handleResponse = (rooms: Room[]) => {
    this.filteredRooms = rooms;
    this.updatePagination();
    this.cdr.detectChanges();
  };

  if (!this.selectedOption && this.selectedFilter !== 'category') return;

  switch (this.selectedFilter) {
    case 'nbBeds':
      this.genericService.fetchFilteredRoomsByNbBeds(Number(this.selectedOption))
        .subscribe(handleResponse);
      break;
    case 'category':
      this.genericService.fetchFilteredRoomsByCategory(this.selectedOption)
        .subscribe(handleResponse);
      break;
    case 'price':
      this.genericService.fetchFilteredRoomsByPrice(Number(this.selectedOption))
        .subscribe(handleResponse);
      break;
  }
}

// applyFilter(): void {
//   console.log("FILTER:", this.selectedFilter);
//   console.log("VALUE:", this.selectedOption);
// }

  getNbBeds(): void {
    this.genericService.fetchNbBedsList()
      .subscribe(data => this.nbBedsList = data);
  }

  getCategories(): void {
    this.genericService.fetchCategories()
      .subscribe(data => this.categories = data);
  }

  getPrices(): void {
    this.genericService.fetchPrices()
      .subscribe(data => this.prices = data);
  }

  getFilteredRoomsByNbBeds(): void {
    this.genericService.fetchFilteredRoomsByNbBeds(Number(this.selectedOption))
      .subscribe(rooms => {
        this.filteredRooms = rooms;
        this.currentPage = 1;
      });
  }

  getFilteredRoomsByCategories(): void {
    this.genericService.fetchFilteredRoomsByCategory(this.selectedOption)
      .subscribe(rooms => {
        this.filteredRooms = rooms;
        this.currentPage = 1;
      });
  }

  getFilteredRoomsByPrice(): void {
    this.genericService.fetchFilteredRoomsByPrice(Number(this.selectedOption))
      .subscribe(rooms => {
        this.filteredRooms = rooms;
        this.currentPage = 1;
      });
  }

updatePagination(): void {
  const start = (this.currentPage - 1) * this.pageSize;
  this.paginatedRooms = this.filteredRooms.slice(start, start + this.pageSize);
}
  get totalPages(): number {
    return Math.ceil(this.filteredRooms.length / this.pageSize);
  }

  nextPage(): void {
  if (this.currentPage < this.totalPages) {
    this.currentPage++;
    this.updatePagination();
  }
}

prevPage(): void {
  if (this.currentPage > 1) {
    this.currentPage--;
    this.updatePagination();
  }
}

// goToPage(page: number): void {
//   this.currentPage = page;
//   this.updatePagination();
// }
}