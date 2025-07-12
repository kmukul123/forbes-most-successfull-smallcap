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

    it('should normalize the provided JSON data correctly', () => {
      const input: ListData = {
        "listName": "2025 AMERICA’S MOST SUCCESSFUL SMALL-CAP COMPANIES",
        "listSubHeading": "NOVEMBER 15, 2024",
        "listCode": "Forbes_America_SmallCap_2024",
        "listCompanies": [
          {
            "RANK": 1,
            "COMPANY": "GigaCloud Technology",
            "INDUSTRY": "Trading Companies",
            "52-WEEK RETURN (%)": 181.6,
            "REVENUE (millions USD)": 1110,
            "year": 2025,
            "TICKER": "GCT",
            "DESCRIPTION": {
              "overview": "GigaCloud Technology operates a global business-to-business (B2B) e-commerce marketplace for large parcel merchandise, such as furniture and home appliances. It connects manufacturers, primarily in Asia, with resellers in the U.S. and Europe. [pos]The company's marketplace GMV increased 56.1% year-over-year to $1,416.7 million for the 12 months ended March 31, 2025.[/pos] The company's moat is its integrated platform combining product discovery, payment, and logistics, creating high switching costs. [link to GigaCloud Technology Announces First Quarter 2025 Financial Results](https://investors.gigacloudtech.com/news-releases/news-release-details/gigacloud-technology-announces-first-quarter-2025-financial) [pos]The company demonstrates strong value creation with a Return on Invested Capital (ROIC) of 17.41% for the TTM as of March 2025, which exceeds its WACC of 6.24%.[/pos] [link to GuruFocus GCT ROIC data](https://www.gurufocus.com/term/roic/NASDAQ:GCT)",
              "insider_ownership": "[pos]Insider ownership is substantial, with CEO Lei Wu holding a 23% stake.[/pos] This aligns leadership with shareholder interests. [link to TipRanks GCT Insider Trading](https://www.tipranks.com/stocks/gct/insider-trading)",
              "balancesheet": "[neg]As of March 31, 2025, GigaCloud had total liabilities of $678.1 million, a significant figure for a potential acquirer.[/neg] [pos]The company has an active share repurchase program of $78 million and has already repurchased $61.8 million worth of shares.[/pos] [link to GigaCloud Technology Announces First Quarter 2025 Financial Results](https://investors.gigacloudtech.com/news-releases/news-release-details/gigacloud-technology-announces-first-quarter-2025-financial)"
            }
          },
          {
            "RANK": 2,
            "COMPANY": "Vital Farms",
            "INDUSTRY": "Food Drink & Tobacco",
            "52-WEEK RETURN (%)": 164,
            "Revenue (millions USD)": 576.1,
            "year": 2025,
            "TICKER": "VITL",
            "DESCRIPTION": {
              "overview": "Vital Farms is an ethical food company that markets and distributes pasture-raised food products, including eggs, butter, and ghee. It partners with a network of over 425 small family farms, emphasizing humane animal treatment and sustainable agriculture. The company has built a powerful brand centered on ethical practices and transparency, which resonates with a growing segment of consumers. [link to Vital Farms Q1 2025 Earnings Release](https://investors.vitalfarms.com/press-releases/press-release-details/2025/Vital-Farms-Reports-First-Quarter-2025-Financial-Results/default.aspx) [pos]Vital Farms demonstrates strong returns on capital, with a Return on Invested Capital (ROIC) of 37.17% and a Return on Capital Employed (ROCE) of 20.43%[/pos]. [link to GuruFocus Vital Farms ROIC/ROCE](https://www.gurufocus.com/stock/VITL/summary)",
              "insider_ownership": "[pos]Insider ownership is significant, at 18.75%[/pos]. [link to GuruFocus Vital Farms Insider Ownership](https://www.gurufocus.com/stock/VITL/insider)",
              "balancesheet": "[pos]Vital Farms has a strong balance sheet, with approximately $161.3 million in cash and no debt as of the first quarter of 2025.[/pos] [link to Vital Farms Q1 2025 Earnings Release](https://investors.vitalfarms.com/press-releases/press-release-details/2025/Vital-Farms-Reports-First-Quarter-2025-Financial-Results/default.aspx)"
            }
          }
        ]
      };

      const expected: ListData = {
        "listName": "2025 AMERICA’S MOST SUCCESSFUL SMALL-CAP COMPANIES",
        "listSubHeading": "NOVEMBER 15, 2024",
        "listCode": "Forbes_America_SmallCap_2024",
        "listCompanies": [
          {
            "RANK": 1,
            "COMPANY": "GigaCloud Technology",
            "INDUSTRY": "Trading Companies",
            "52-WEEK RETURN (%)": 181.6,
            "REVENUE (MILLIONS USD)": 1110,
            "YEAR": 2025,
            "TICKER": "GCT",
            "DESCRIPTION": {
              "OVERVIEW": "GigaCloud Technology operates a global business-to-business (B2B) e-commerce marketplace for large parcel merchandise, such as furniture and home appliances. It connects manufacturers, primarily in Asia, with resellers in the U.S. and Europe. [pos]The company's marketplace GMV increased 56.1% year-over-year to $1,416.7 million for the 12 months ended March 31, 2025.[/pos] The company's moat is its integrated platform combining product discovery, payment, and logistics, creating high switching costs. [link to GigaCloud Technology Announces First Quarter 2025 Financial Results](https://investors.gigacloudtech.com/news-releases/news-release-details/gigacloud-technology-announces-first-quarter-2025-financial) [pos]The company demonstrates strong value creation with a Return on Invested Capital (ROIC) of 17.41% for the TTM as of March 2025, which exceeds its WACC of 6.24%.[/pos] [link to GuruFocus GCT ROIC data](https://www.gurufocus.com/term/roic/NASDAQ:GCT)",
              "INSIDER_OWNERSHIP": "[pos]Insider ownership is substantial, with CEO Lei Wu holding a 23% stake.[/pos] This aligns leadership with shareholder interests. [link to TipRanks GCT Insider Trading](https://www.tipranks.com/stocks/gct/insider-trading)",
              "BALANCESHEET": "[neg]As of March 31, 2025, GigaCloud had total liabilities of $678.1 million, a significant figure for a potential acquirer.[/neg] [pos]The company has an active share repurchase program of $78 million and has already repurchased $61.8 million worth of shares.[/pos] [link to GigaCloud Technology Announces First Quarter 2025 Financial Results](https://investors.gigacloudtech.com/news-releases/news-release-details/gigacloud-technology-announces-first-quarter-2025-financial)"
            }
          },
          {
            "RANK": 2,
            "COMPANY": "Vital Farms",
            "INDUSTRY": "Food Drink & Tobacco",
            "52-WEEK RETURN (%)": 164,
            "REVENUE (MILLIONS USD)": 576.1,
            "YEAR": 2025,
            "TICKER": "VITL",
            "DESCRIPTION": {
              "OVERVIEW": "Vital Farms is an ethical food company that markets and distributes pasture-raised food products, including eggs, butter, and ghee. It partners with a network of over 425 small family farms, emphasizing humane animal treatment and sustainable agriculture. The company has built a powerful brand centered on ethical practices and transparency, which resonates with a growing segment of consumers. [link to Vital Farms Q1 2025 Earnings Release](https://investors.vitalfarms.com/press-releases/press-release-details/2025/Vital-Farms-Reports-First-Quarter-2025-Financial-Results/default.aspx) [pos]Vital Farms demonstrates strong returns on capital, with a Return on Invested Capital (ROIC) of 37.17% and a Return on Capital Employed (ROCE) of 20.43%[/pos]. [link to GuruFocus Vital Farms ROIC/ROCE](https://www.gurufocus.com/stock/VITL/summary)",
              "INSIDER_OWNERSHIP": "[pos]Insider ownership is significant, at 18.75%[/pos]. [link to GuruFocus Vital Farms Insider Ownership](https://www.gurufocus.com/stock/VITL/insider)",
              "BALANCESHEET": "[pos]Vital Farms has a strong balance sheet, with approximately $161.3 million in cash and no debt as of the first quarter of 2025.[/pos] [link to Vital Farms Q1 2025 Earnings Release](https://investors.vitalfarms.com/press-releases/press-release-details/2025/Vital-Farms-Reports-First-Quarter-2025-Financial-Results/default.aspx)"
            }
          }
        ]
      };
      expect(normalizeData(input)).toEqual(expected);
    });
  });
});