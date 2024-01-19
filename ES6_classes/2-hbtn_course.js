/* eslint-disable */
export default class HolbertonCourse {
    constructor(name, length, students) {
      this._name = HolbertonCourse.validateString(name, 'Name');
      this._length = HolbertonCourse.validateNumber(length, 'Length');
      this._students = HolbertonCourse.validateArray(students, 'Students');
    }
  
    get name() {
      return this._name;
    }
  
    set name(new_name) {
      this._name = HolbertonCourse.validateString(new_name, 'Name');
    }
  
    get length() {
      return this._length;
    }
  
    set length(new_length) {
      this._length = HolbertonCourse.validateNumber(new_length, 'Length');
    }
  
    get students() {
      return this._students;
    }
  
    set students(new_students) {
      this._students = HolbertonCourse.validateArray(new_students, 'Students');
    }
  
    static validateString(value, propertyName) {
      if (typeof value !== 'string') {
        throw new TypeError(`${propertyName} Must be a string`);
      }
      return value;
    }
  
    static validateNumber(value, propertyName) {
      if (typeof value !== 'number') {
        throw new TypeError(`${propertyName} Must be a number`);
      }
      return value;
    }
  
    static validateArray(value, propertyName) {
      if (!Array.isArray(value)) {
        throw new TypeError(`${propertyName} Must be an array`);
      }
      return value;
    }
  }