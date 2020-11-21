from django.shortcuts import render
from .forms import MatchForm,TeamrankForm,totalTeamrankForm
from .models import match,teamrank,totalteamrank
from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Sum

# Create your views here.


def matchplayed(request):
    rank=teamrank.objects.all().order_by('-id')
    matches=match.objects.all().order_by('-id')
    form = MatchForm(request.POST or None, request.FILES or None)
    form1 = TeamrankForm(request.POST or None, request.FILES or None)
    form2 = totalTeamrankForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        match0 = form.save(commit=False)
        tour = form.cleaned_data['tournament_name']
        team_a = form.cleaned_data['team_a']
        team_b = form.cleaned_data['team_b']
        team_goal_a = form.cleaned_data['team_a_goals']
        team_goal_b = form.cleaned_data['team_b_goals']
        date = form.cleaned_data['date']
        time = form.cleaned_data['time']
        if team_goal_a > team_goal_b:
            match0.winner = team_a;
        else:
            match0.winner = team_b;
        match0.save()
        if teamrank.objects.filter(teamown=team_a,tournament_name=tour).exists():
            instance1 = get_object_or_404(teamrank, teamown=team_a,tournament_name=tour)
            formone=TeamrankForm(request.POST or None, request.FILES or None,instance=instance1,prefix="form1")
        else:
            formone=TeamrankForm(request.POST or None, request.FILES or None,prefix="form1")
        user = formone.save(commit=False)

        user.tournament_name=tour
        user.teamown = team_a
        user.teamname =str(team_a)

        goal11=match.objects.filter(team_a=team_a,tournament_name=tour).aggregate(sum=Sum('team_a_goals'))['sum']
        goal12=match.objects.filter(team_b=team_a,tournament_name=tour).aggregate(sum=Sum('team_b_goals'))['sum']
        if goal11 is None:
            goal11=0
        if goal12 is None:
            goal12=0
        goal1 = int(goal11) + int(goal12)
        print(goal1)
        user.teamgoals = goal1

        matchtotal11 = match.objects.filter(team_a=team_a,tournament_name=tour).count()
        matchtotal12 = match.objects.filter(team_b=team_a,tournament_name=tour).count()
        matchtotal1 = matchtotal11 + matchtotal12
        user.matchs_played = matchtotal1
         

        matchwon11 = match.objects.filter(winner=team_a,team_a=team_a,tournament_name=tour).count()
        matchwon12 = match.objects.filter(winner=team_a,team_b=team_a,tournament_name=tour).count()
        matchwon1 = matchwon11 + matchwon12
        user.match_won = matchwon1

        matchlost1 = matchwon1
        user.match_lost = matchtotal1 - matchlost1
        user.save()


        if teamrank.objects.filter(teamown=team_b,tournament_name=tour).exists():
            instance1 = get_object_or_404(teamrank, teamown=team_b,tournament_name=tour)
            formone=TeamrankForm(request.POST or None, request.FILES or None,instance=instance1,prefix="form1")
        else:
            formone=TeamrankForm(request.POST or None, request.FILES or None,prefix="form1")

        user = formone.save(commit=False)
        user.tournament_name=tour
        user.teamown = team_b
        user.teamname =str(team_b)

        goal21=match.objects.filter(team_a=team_b,tournament_name=tour).aggregate(sum=Sum('team_a_goals'))['sum']
        goal22=match.objects.filter(team_b=team_b,tournament_name=tour).aggregate(sum=Sum('team_b_goals'))['sum']
        if goal21 is None:
            goal21=0
        if goal22 is None:
            goal22=0
        goal2 = int(goal21) + int(goal22)
        print(goal2)
        user.teamgoals = goal2

        matchtotal21 = match.objects.filter(team_a=team_b,tournament_name=tour).count()
        matchtotal22 = match.objects.filter(team_b=team_b,tournament_name=tour).count()
        matchtotal2 = matchtotal21 + matchtotal22
        user.matchs_played = matchtotal2
         

        matchwon21 = match.objects.filter(winner=team_b,team_a=team_b,tournament_name=tour).count()
        matchwon22 = match.objects.filter(winner=team_b,team_b=team_b,tournament_name=tour).count()
        matchwon2 = matchwon21 + matchwon22
        user.match_won = matchwon2

        matchlost2 = matchwon2
        user.match_lost = matchtotal2 - matchlost2
        user.save()


        if totalteamrank.objects.filter(teamown=team_a).exists():
            instance2 = get_object_or_404(totalteamrank, teamown=team_a)
            formtwo=totalTeamrankForm(request.POST or None, request.FILES or None,instance=instance2,prefix="form2")
        else:
            formtwo=totalTeamrankForm(request.POST or None, request.FILES or None,prefix="form2")
        user2 = formtwo.save(commit=False)

        user2.teamown = team_a
        user2.teamname =str(team_a)

        goal11=match.objects.filter(team_a=team_a).aggregate(sum=Sum('team_a_goals'))['sum']
        goal12=match.objects.filter(team_b=team_a).aggregate(sum=Sum('team_b_goals'))['sum']
        if goal11 is None:
            goal11=0
        if goal12 is None:
            goal12=0
        goal1 = int(goal11) + int(goal12)
        print(goal1)
        user2.teamgoals = goal1

        matchtotal11 = match.objects.filter(team_a=team_a).count()
        matchtotal12 = match.objects.filter(team_b=team_a).count()
        matchtotal1 = matchtotal11 + matchtotal12
        user2.matchs_played = matchtotal1
         

        matchwon11 = match.objects.filter(winner=team_a,team_a=team_a).count()
        matchwon12 = match.objects.filter(winner=team_a,team_b=team_a).count()
        matchwon1 = matchwon11 + matchwon12
        user2.match_won = matchwon1

        matchlost1 = matchwon1
        user2.match_lost = matchtotal1 - matchlost1
        user2.save()


        if totalteamrank.objects.filter(teamown=team_b).exists():
            instance2 = get_object_or_404(totalteamrank, teamown=team_b)
            formtwo=totalTeamrankForm(request.POST or None, request.FILES or None,instance=instance2,prefix="form2")
        else:
            formtwo=totalTeamrankForm(request.POST or None, request.FILES or None,prefix="form2")

        user2 = formtwo.save(commit=False)
        user2.teamown = team_b
        user2.teamname =str(team_b)

        goal21=match.objects.filter(team_a=team_b).aggregate(sum=Sum('team_a_goals'))['sum']
        goal22=match.objects.filter(team_b=team_b).aggregate(sum=Sum('team_b_goals'))['sum']
        if goal21 is None:
            goal21=0
        if goal22 is None:
            goal22=0
        goal2 = int(goal21) + int(goal22)
        print(goal2)
        user2.teamgoals = goal2

        matchtotal21 = match.objects.filter(team_a=team_b).count()
        matchtotal22 = match.objects.filter(team_b=team_b).count()
        matchtotal2 = matchtotal21 + matchtotal22
        user2.matchs_played = matchtotal2
         

        matchwon21 = match.objects.filter(winner=team_b,team_a=team_b).count()
        matchwon22 = match.objects.filter(winner=team_b,team_b=team_b).count()
        matchwon2 = matchwon21 + matchwon22
        user2.match_won = matchwon2

        matchlost2 = matchwon2
        user2.match_lost = matchtotal2 - matchlost2
        user2.save()



       
    rank=teamrank.objects.all().order_by('-id')
    matches=match.objects.all().order_by('-id')
    ttrank=totalteamrank.objects.all().order_by('-id')
    context = {
        'form': form,
        'teamrank':rank,
        "match":matches,
        "ttr": ttrank
    }
    return render(request, 'match.html', context)


def deletematch(request,id):
    matches = match.objects.get(pk=id)
    team_a=matches.team_a
    team_b=matches.team_b
    tour=matches.tournament_name
    matches.delete()
    form1 = TeamrankForm(request.POST or None, request.FILES or None)
    form2 = totalTeamrankForm(request.POST or None, request.FILES or None)

    if teamrank.objects.filter(teamown=team_a,tournament_name=tour).exists():
        instance1 = get_object_or_404(teamrank, teamown=team_a,tournament_name=tour)
        formone=TeamrankForm(request.POST or None, request.FILES or None,instance=instance1,prefix="form1")
    else:
        formone=TeamrankForm(request.POST or None, request.FILES or None,prefix="form1")
    
    user = formone.save(commit=False)
    user.tournament_name=tour
    user.teamown = team_a
    user.teamname =str(team_a)

    goal11=match.objects.filter(team_a=team_a,tournament_name=tour).aggregate(sum=Sum('team_a_goals'))['sum']
    goal12=match.objects.filter(team_b=team_a,tournament_name=tour).aggregate(sum=Sum('team_b_goals'))['sum']
    if goal11 is None:
        goal11=0
    if goal12 is None:
        goal12=0
    goal1 = int(goal11) + int(goal12)
    print(goal1)
    user.teamgoals = goal1

    matchtotal11 = match.objects.filter(team_a=team_a,tournament_name=tour).count()
    matchtotal12 = match.objects.filter(team_b=team_a,tournament_name=tour).count()
    matchtotal1 = matchtotal11 + matchtotal12
    user.matchs_played = matchtotal1
        

    matchwon11 = match.objects.filter(winner=team_a,team_a=team_a,tournament_name=tour).count()
    matchwon12 = match.objects.filter(winner=team_a,team_b=team_a,tournament_name=tour).count()
    matchwon1 = matchwon11 + matchwon12
    user.match_won = matchwon1

    matchlost1 = matchwon1
    user.match_lost = matchtotal1 - matchlost1
    user.save()


    if teamrank.objects.filter(teamown=team_b,tournament_name=tour,).exists():
        instance1 = get_object_or_404(teamrank, teamown=team_b,tournament_name=tour)
        formone=TeamrankForm(request.POST or None, request.FILES or None,instance=instance1,prefix="form1")
    else:
        formone=TeamrankForm(request.POST or None, request.FILES or None,prefix="form1")

    user.tournament_name=tour
    user = formone.save(commit=False)
    user.teamown = team_b
    user.teamname =str(team_b)

    goal21=match.objects.filter(team_a=team_b,tournament_name=tour).aggregate(sum=Sum('team_a_goals'))['sum']
    goal22=match.objects.filter(team_b=team_b,tournament_name=tour).aggregate(sum=Sum('team_b_goals'))['sum']
    if goal21 is None:
        goal21=0
    if goal22 is None:
        goal22=0
    goal2 = int(goal21) + int(goal22)
    print(goal2)
    user.teamgoals = goal2

    matchtotal21 = match.objects.filter(team_a=team_b,tournament_name=tour).count()
    matchtotal22 = match.objects.filter(team_b=team_b,tournament_name=tour).count()
    matchtotal2 = matchtotal21 + matchtotal22
    user.matchs_played = matchtotal2
        

    matchwon21 = match.objects.filter(winner=team_b,team_a=team_b,tournament_name=tour).count()
    matchwon22 = match.objects.filter(winner=team_b,team_b=team_b,tournament_name=tour).count()
    matchwon2 = matchwon21 + matchwon22
    user.match_won = matchwon2

    matchlost2 = matchwon2
    user.match_lost = matchtotal2 - matchlost2
    user.save()




    if totalteamrank.objects.filter(teamown=team_a).exists():
        instance2 = get_object_or_404(totalteamrank, teamown=team_a)
        formtwo=totalTeamrankForm(request.POST or None, request.FILES or None,instance=instance2,prefix="form2")
    else:
        formtwo=totalTeamrankForm(request.POST or None, request.FILES or None,prefix="form2")
    user2 = formtwo.save(commit=False)

    user2.teamown = team_a
    user2.teamname =str(team_a)

    goal11=match.objects.filter(team_a=team_a).aggregate(sum=Sum('team_a_goals'))['sum']
    goal12=match.objects.filter(team_b=team_a).aggregate(sum=Sum('team_b_goals'))['sum']
    if goal11 is None:
        goal11=0
    if goal12 is None:
        goal12=0
    goal1 = int(goal11) + int(goal12)
    print(goal1)
    user2.teamgoals = goal1

    matchtotal11 = match.objects.filter(team_a=team_a).count()
    matchtotal12 = match.objects.filter(team_b=team_a).count()
    matchtotal1 = matchtotal11 + matchtotal12
    user2.matchs_played = matchtotal1
        

    matchwon11 = match.objects.filter(winner=team_a,team_a=team_a).count()
    matchwon12 = match.objects.filter(winner=team_a,team_b=team_a).count()
    matchwon1 = matchwon11 + matchwon12
    user2.match_won = matchwon1

    matchlost1 = matchwon1
    user2.match_lost = matchtotal1 - matchlost1
    user2.save()


    if totalteamrank.objects.filter(teamown=team_b).exists():
        instance2 = get_object_or_404(totalteamrank, teamown=team_b)
        formtwo=totalTeamrankForm(request.POST or None, request.FILES or None,instance=instance2,prefix="form2")
    else:
        formtwo=totalTeamrankForm(request.POST or None, request.FILES or None,prefix="form2")

    user2 = formtwo.save(commit=False)
    user2.teamown = team_b
    user2.teamname =str(team_b)

    goal21=match.objects.filter(team_a=team_b).aggregate(sum=Sum('team_a_goals'))['sum']
    goal22=match.objects.filter(team_b=team_b).aggregate(sum=Sum('team_b_goals'))['sum']
    if goal21 is None:
        goal21=0
    if goal22 is None:
        goal22=0
    goal2 = int(goal21) + int(goal22)
    print(goal2)
    user2.teamgoals = goal2

    matchtotal21 = match.objects.filter(team_a=team_b).count()
    matchtotal22 = match.objects.filter(team_b=team_b).count()
    matchtotal2 = matchtotal21 + matchtotal22
    user2.matchs_played = matchtotal2
        

    matchwon21 = match.objects.filter(winner=team_b,team_a=team_b).count()
    matchwon22 = match.objects.filter(winner=team_b,team_b=team_b).count()
    matchwon2 = matchwon21 + matchwon22
    user2.match_won = matchwon2

    matchlost2 = matchwon2
    user2.match_lost = matchtotal2 - matchlost2
    user.save()




    
    return redirect('matchplayed')


