#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool is_number (char* num);
bool validation (char* num);
void print_card_brand(char* num);

int main() {
     while (true) {
          printf("Please Enter Number of your card: ");
          char num[20];
          scanf("%s", &num);
          if(is_number(num))
               if (validation(num))  
                    print_card_brand(num);
          else printf("INVALID\n");
          printf("another check ? (y/n): ");
          char c;
          scanf("\n%c", &c);
          if (c != 'y') {
               printf("Thanks for using our system !");
               break;
          }
     }
     return 0;
}

bool is_number (char* num) {
     bool flag = true;
     for(int i = 0; i < strlen(num); i++) 
          if(num[i] < 48 || num[i] > 57) flag = false;
     return flag;
}

bool validation (char* num) {
     int first_checksum = 0, second_checksum = 0;
     for(int i = strlen(num) - 1; i >= 0; i--){
          int tmp_digit = (num[i] - '0');
          if (i & 1) {
               first_checksum += tmp_digit;
               tmp_digit *= 2;
               second_checksum += (tmp_digit / 10 + tmp_digit % 10);
          }
          else {
               second_checksum += tmp_digit;
               tmp_digit *= 2;
               first_checksum += (tmp_digit / 10 + tmp_digit % 10);
          }
     }
     if((first_checksum % 10 == 0 || second_checksum % 10 == 0) && strlen(num) >= 13) return true;
     else return false;
}

void print_card_brand(char* num) {
     if(num[0] == '3' && (num[1] == '4' || num[1] == '7')) printf("AMEX\n");
     else if(num[0] == '5' && num[1] - '0' <= 5) printf("MASTERCARD\n");
     else if(num[0] == '4') printf("VISA\n");
     else printf("INVALID\n");
}