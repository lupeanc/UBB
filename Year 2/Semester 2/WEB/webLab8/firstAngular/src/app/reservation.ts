// import {Room} from './room';

export interface Reservation {
    id: number;
    user_id: number;
    room_id: number;
    start: string;
    end: string;
}