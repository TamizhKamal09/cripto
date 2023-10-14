import datetime
import hashlib
import logging
import pdb
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime, timedelta
import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from members.models import Account_Detils, Block, User, chat_messagers
from django.utils import timezone

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('user')  # Use 'user' as the name attribute in your HTML form
        password = request.POST.get('pass')  # Use 'pass' as the name attribute in your HTML form

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home URL pattern
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login_view')  # Redirect back to the login page if authentication fails

    return render(request, 'login.html')


def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password1 = request.POST.get('pass1')  # Use 'pass1' as the name attribute in your HTML form
        password2 = request.POST.get('pass2')  # Use 'pass2' as the name attribute in your HTML form
        email = request.POST.get('email')

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup_view')

        # Create a new user
        user = User.objects.create_user(username=username, password=password1, email=email)

        if user is not None:
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('home')  # Redirect to the home page after successful registration
        else:
            messages.error(request, 'Registration failed.')
            return redirect('sign_up')  # Redirect back to the registration page if registration fails

    return render(request, 'login.html')  


def crypto_chart():
    # Fetch historical crypto data from an API (e.g., CoinGecko)
    api_url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",
        "days": 365,  # Fetch data for the last year
    }
    
    response = requests.get(api_url, params=params)
    print(response.status_code, "<----------------- response.status_code")
    if response.status_code == 200:
        crypto_data = response.json()
        formatted_data = []
        for entry in crypto_data['prices']:
            print(entry,"entrys")
            timestamp_ms = entry[0]
            price = entry[1]
            
            # Convert timestamp (milliseconds since epoch) to a Python datetime object
            date = datetime.utcfromtimestamp(timestamp_ms / 1000).strftime('%Y-%m-%d')
            
            formatted_data.append([date, price])
        print(formatted_data,"<=------------------------------------ formatted_data")
        return formatted_data


import requests
from datetime import datetime, timedelta

def crypto_table():
    # Calculate the timestamp for one year ago in seconds
    one_year_ago = datetime.now() - timedelta(days=365)
    timestamp_one_year_ago_in_seconds = int(one_year_ago.timestamp())

    # Fetch historical crypto data for the last year from the CoinGecko API
    api_url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart_range"
    params = {
        "vs_currency": "usd",
        "from": timestamp_one_year_ago_in_seconds,
        "to": int(datetime.now().timestamp()),
        "interval": "daily",
    }

    try:
        response = requests.get(api_url, params=params)
        print(response.status_code, "<----------------- response.status_code")
        if response.status_code == 200:
            crypto_data = response.json()
            formatted_data = []
            for entry in crypto_data['prices']:
                print(entry,"entrys")
                timestamp_ms = entry[0]
                price = entry[1]
                
                # Convert timestamp (milliseconds since epoch) to a Python datetime object
                date = datetime.utcfromtimestamp(timestamp_ms / 1000).strftime('%Y-%m-%d')
                
                formatted_data.append([date, price])
            print(formatted_data,"<=------------------------------------ formatted_data")
            return formatted_data
        else:
            crypto_data = []
            return crypto_data

    except Exception as e:
        # Handle exceptions and errors here
        print(f"Error: {e}")
        crypto_data = []
        return crypto_data


def home(request):
    crypto_data = crypto_chart()
    return render(request, "home.html", {'crypto_data': crypto_data})


def chat_view(request):
    print("000000000000000000000000000000000000000000000")
    current_user = request.user  # Get the current user
    print(current_user.id, "0000000000000000000000")
    user_name = current_user.username
    if request.method == 'POST':
        message = request.POST.get('message')
        print(message, " user_id 000000000000000000000000000000000000000000000")
        try:
            chat_messagers.objects.create(userid=current_user, messages=message,user_name = user_name)
            print("Data saved successfully")
        except IntegrityError as e:
            print(f"Error saving data: {e}")
        
    message = chat_messagers.objects.all()
    data = User.objects.all()
    
    
    
    return render(request, 'chat.html', {"data": data,"message":message})




# def message(request, id):
#     user = User.objects.filter(id=id).first()  # Use .first() to get the first matching user
#     current_user = request.user  # Get the current user
#     total = total_amount(request)
#     if request.method == 'POST':
#         user = User.objects.filter(id = id).first()
#         if user:
#             user_name_db = user.username
#         else:
#             user_name_db = None
#             print("User Name Mismatching..... try another id..")
#         amount = request.POST.get('amount')
#         print(id," =============111111============> user_id")
#         print(amount," ==============111111===========> amount")
#         amount = int(total) - int(amount)
         
#         if amount:
        
#             Account_Detils.objects.create(username = user_name_db, user_id = id,cripto_amount   = amount)
#             print("Data saved successfully")
#             return redirect('cripto')
#         else:
            
#             print("your account amount low")
        
#     return render(request, 'message.html', {'user': user})


# def message(request, id):
#     user = User.objects.filter(id=id).first()
#     print(user,"<-------------------- user")
#     current_user = request.user
#     current_user_id = current_user.id
#     print(current_user.id, "<------------------------------- current_user.id")
#     print(current_user.username, "<------------------------------- current_user.username")
#     current_user_username = current_user.username
#     total = total_amount(request)
    
#     if request.method == 'POST':
#         user = User.objects.filter(id=id).first()
#         print(user,"<------------------- user2")
        
#         if user:
#             user_name_db = user.username
#         else:
#             user_name_db = None
#             print("User Name Mismatching... Try another id...")
        
        
#         print(user_name_db,"<------------------ user_name_db")
#         amount = request.POST.get('amount')
#         print(amount,"<------------------ amount")
        
#         if amount is not None:
#             try:
#                 amount = int(amount)
#             except ValueError:
#                 print("Invalid amount. Please enter a valid positive integer.")
#                 return redirect('cripto')
            
#             if amount > 0:
#                 print(total,"<----------------- total")
#                 updated_amount = total - amount
#                 print(updated_amount,"<----------------- updated_amount")
#                 if updated_amount >= 0:
#                     Account_Detils.objects.create(username=current_user_username, user_id=current_user_id, cripto_amount = -amount)
#                     Account_Detils.objects.create(username=user_name_db, user_id=id, cripto_amount=amount)
#                     print("Data saved successfully")
#                     return JsonResponse({'success': True})
#                 else:
#                     print("Your account amount is low")
#                     return JsonResponse({'success': False, 'error_message': 'Your account amount is low'})
#             else:
#                 print("Amount should be a positive integer.")
#         else:
#             print("Amount is missing in the POST data.")
    
#     return render(request, 'message.html', {'user': user})


def message(request, id):
    user = User.objects.filter(id=id).first()
    print(user, "<-------------------- user")
    current_user = request.user
    current_user_id = current_user.id
    print(current_user.id, "<------------------------------- current_user.id")
    print(current_user.username, "<------------------------------- current_user.username")
    current_user_username = current_user.username
    total = total_amount(request)
    if request.method == 'POST':
        user = User.objects.filter(id=id).first()
        print(user, "<------------------- user2")

        if user:
            user_name_db = user.username
        else:
            user_name_db = None
            print("User Name Mismatching... Try another id...")

        print(user_name_db, "<------------------ user_name_db")
        amount = request.POST.get('amount')
        print(amount, "<------------------ amount")

        if amount is not None:
            try:
                amount = int(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid positive integer.")
                return redirect('cripto')

            if amount > 0:
                print(total, "<----------------- total")
                updated_amount = total - amount
                print(updated_amount, "<----------------- updated_amount")
                if updated_amount >= 0:
                    try:
                        last_block = Block.objects.latest('timestamp')
                    except Block.DoesNotExist:
                        last_block = None
                    print(last_block, "<-------------- last_block 11111111111")

                    if last_block:
                        previous_hash = last_block.compute_hash()
                    else:
                        # Handle the case when there's no previous block, such as the genesis block
                        previous_hash = ''
                    print(previous_hash, "<-------------- previous_hash 2222222222222222222")

                    if last_block is not None:
                        last_proof = last_block.nonce
                    else:
                        # Handle the case when there are no blocks yet (e.g., for the genesis block)
                        last_proof = 0
                    nonce=proof_of_work(last_proof),
                    nonce = nonce[0]
                    
                    
                    print(current_user_id,"< -------------------- current_user_id")
                    print(previous_hash,"< -------------------- previous_hash")
                    print(timezone.now(),"< -------------------- timezone.now()")
                    print(nonce,"< -------------------- nonce")
                    print(amount,"< -------------------- amount")
                    
                    # Block.objects.create(index=current_user_id,timestamp=timezone.now(),previous_hash=previous_hash,data=amount,nonce=nonce)
                    
                    new_block = Block(
                        index=current_user_id,  # Set the index based on your logic
                        timestamp=timezone.now(),
                        previous_hash=previous_hash,
                        data=amount,
                        nonce=nonce
                    )
                    
                    try:
                        new_block.save()
                    except:
                        pass

                    
                    print("Transaction saved as a new block in the blockchain")
                    account_details = Account_Detils.objects.create(
                        username=current_user_username,
                        user_id=current_user_id,
                        cripto_amount=-amount,
                    )
                    # account_details.save()

                    Account_Detils.objects.create(
                        username=user_name_db,
                        user_id=id,
                        cripto_amount=amount,
                    )
                    print("Data saved successfully")
                    return JsonResponse({'success': True})
                else:
                    print("Your account amount is low")
                    return JsonResponse({'success': False, 'error_message': 'Your account amount is low'})
            else:
                print("Amount should be a positive integer.")
        else:
            print("Amount is missing in the POST data.")

    return render(request, 'message.html', {'user': user})


def proof_of_work(last_proof, difficulty=4):
    proof = 0
    while not is_valid_proof(last_proof, proof, difficulty):
        proof += 1
    return proof

def is_valid_proof(last_proof, proof, difficulty):
    guess = f"{last_proof}{proof}".encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:difficulty] == '0' * difficulty


def block_chain(request):
    data = Block.objects.all()
    return render(request, 'block_chain.html',{"data":data})


def timer(request):
    return render(request, 'timer.html')


def total_amount(request):
    current_user = request.user  # Get the current user
    print(current_user.id, "0000000000000000000000")
    amount = Account_Detils.objects.filter(user_id = current_user.id).all()
    total = 0
    for i in amount:
        print(i.cripto_amount)
        amount_i = i.cripto_amount
        if amount_i and amount_i.strip():  # Check if amount_i is not empty
            try:
                total += int(amount_i)  # Add each element to the total if it's a valid integer
            except ValueError:
                pass  # Handle the case where amount_i cannot be converted to an integer
    
    print(total, "000000000000000000000000000000000000")
    return total



def profile(request):
    current_user = request.user  # Get the current user
    current_user_id = current_user.id
    current_user_name = current_user.username
    print(current_user.id, "<-------------------------- = current user id user")
    if request.method == 'POST':
        amount = request.POST.get('amount')
        print(amount,"0 amount amount amount 00000000000000000000000000000000000000000000")
        Account_Detils.objects.create(
            username=current_user_name,
            user_id=current_user_id,
            cripto_amount=amount,
        )
        
    user = User.objects.filter(id=current_user.id).first()
    total = total_amount(request)
    return render(request, 'profile.html', {'user': user,"amount":total})




def cripto(request):
    current_user = request.user  # Get the current user
    print(current_user.id, "0000000000000000000000")
    user_name = current_user.username
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = User.objects.filter(id = user_id).first()
        if user:
            user_name_db = user.username
        else:
            user_name_db = None
            print("User Name Mismatching..... try another id..")
        amount = request.POST.get('amount')
        user_name = request.POST.get('user_name')
        
        print(user_id," =============111111============> user_id")
        print(amount," ==============111111===========> amount")
        print(user_name," ===========111111==============> user_name")
        
    message = chat_messagers.objects.all()
    data = User.objects.all()

    return render(request, 'cripto.html',  {"data": data,"message":message})


