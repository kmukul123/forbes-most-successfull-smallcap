import { TestBed } from '@angular/core/testing';
import { Data, ListData } from './data';
import { HttpClientTestingModule } from '@angular/common/http/testing';

// Private functions exported for testing
import { normalizeData, normalizeKeysToUppercase } from './data';

describe('Data Service and Normalization Functions', () => {
  let service: Data;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [Data],
    });
    service = TestBed.inject(Data);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  describe('normalizeKeysToUppercase', () => {
    it('should convert all keys in a simple object to uppercase', () => {
      const input = { name: 'John', age: 30 };
      const expected = { NAME: 'John', AGE: 30 };
      expect(normalizeKeysToUppercase(input)).toEqual(expected);
    });

    it('should handle nested objects', () => {
      const input = { person: { name: 'Jane', age: 25 }, city: 'New York' };
      const expected = { PERSON: { NAME: 'Jane', AGE: 25 }, CITY: 'New York' };
      expect(normalizeKeysToUppercase(input)).toEqual(expected);
    });

    it('should handle arrays of objects', () => {
      const input = {
        people: [{ name: 'Jack', age: 40 }, { name: 'Jill', age: 35 }],
      };
      const expected = {
        PEOPLE: [{ NAME: 'Jack', AGE: 40 }, { NAME: 'Jill', AGE: 35 }],
      };
      expect(normalizeKeysToUppercase(input)).toEqual(expected);
    });

    it('should return the same object if it is not a plain object or array', () => {
      const input = 'a string';
      expect(normalizeKeysToUppercase(input)).toBe(input);
    });

    it('should handle complex nested structures', () => {
      const input = {
        level1: {
          level2: { key: 'value', arr: [1, { nestedKey: 'nestedValue' }] },
        },
      };
      const expected = {
        LEVEL1: {
          LEVEL2: { KEY: 'value', ARR: [1, { NESTEDKEY: 'nestedValue' }] },
        },
      };
      expect(normalizeKeysToUppercase(input)).toEqual(expected);
    });
  });

  describe('normalizeData', () => {
    it('should normalize the keys of each company in listCompanies to uppercase', () => {
      const input: ListData = {
        listName: 'Test List',
        listSubHeading: 'Test Subheading',
        listCode: 'test',
        listCompanies: [
          { name: 'Company A', rank: 1 },
          { name: 'Company B', rank: 2 },
        ],
      };
      const expected: ListData = {
        listName: 'Test List',
        listSubHeading: 'Test Subheading',
        listCode: 'test',
        listCompanies: [
          { NAME: 'Company A', RANK: 1 },
          { NAME: 'Company B', RANK: 2 },
        ],
      };
      expect(normalizeData(input)).toEqual(expected);
    });

    it('should handle an empty list of companies', () => {
      const input: ListData = {
        listName: 'Empty List',
        listSubHeading: 'Empty Subheading',
        listCode: 'empty',
        listCompanies: [],
      };
      const expected: ListData = {
        listName: 'Empty List',
        listSubHeading: 'Empty Subheading',
        listCode: 'empty',
        listCompanies: [],
      };
      expect(normalizeData(input)).toEqual(expected);
    });
  });
});