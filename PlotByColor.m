%import Data
M = readtable('/home/elad/reboundx-csv/3jupiters_tides/output.aei.time-100.csv');
M = table2array(M);
%%
%IF THE FIRST COLOM IS TIME THEN WE DUMP IT [if there are diffrent value
%there, it might be a problem with some rows
% M(:,1) = [];

M = sortrows(M,1);
%DIVADERES OF DIFFENT POPULATIONS BY EYE ESTIMATE
a = [0,3.5,7,20,Inf];
%a = [0,Inf];

c1= [12/255 123/255 220/255];
c2= [255/255 194/255 10/255];
c3= [153/255 79/255 0/255];
c4= [93/255 58/255 155/255];
c5= [225/255 190/255 106/255];
c6= [64/255 176/255 166/255];
c7= [230/255 97/255 0/255];
c8= [0/255 108/255 209/255];
% 8 MORE COLORS
% c9= [26/255 255/255 26/255];
% c10= [75/255 0/255 146/255];
% c11= [254/255 254/255 98/255];
% c12= [211/255 95/255 183/255];
% c13= [0/255 90/255 181/255];
% c14= [220/255 50/255 32/255];
% c15= [26/255 133/255 255/255];
% c16= [212/255 17/255 89/255];
CL = [c1; c2; c3; c4; c5; c6; c7; c8];

% IF NEED MORE COLORS
%CL = rand(length(a)-1,3);

figure(1);
subplot(2,1,1);
hold on
for i=1:length(a)-1
    Mtemp = M;
    Ind = find(a(i)<= Mtemp(:,1) & Mtemp(:,1)<a(i+1));
    Mtemp= Mtemp(Ind,:);
    Num = size(Mtemp,1);
    Yaxis = 1:Num;
    c = CL(i,:);
    %     scatter(Mtemp(:,1),Yaxis,[],c,'x');%,c,CL(:,i))
    [~,edges] = histcounts(log10(Mtemp(:,1)));
    histogram(Mtemp(:,1),10.^edges,'FaceColor',c)
    %     plot(Mtemp(:,1),c)
end
legend('0<a<3.5','3.5<a<7','7<a<20','20<a');
xlabel('a[AU]');
ylabel('num');
set(gca,'xscale','log')
hold off

subplot(2,1,2);
hold on
for i=1:length(a)-1
    Mtemp = M;
    Ind = find(a(i)<= Mtemp(:,1) & Mtemp(:,1)<a(i+1));
    Mtemp= Mtemp(Ind,:);
    Num = size(Mtemp,1);
    Mtemp = sortrows(Mtemp,1);
    c = CL(i,:);
    plot(Mtemp(:,1),((1:Num)/Num),'color',c)
end
set(gca,'xscale','log')
legend('0<a<3.5','3.5<a<7','7<a<20','20<a');
xlabel('a[AU]');
ylabel('cdf');
saveas(figure(1),'a_distribution.jpg')
hold off

figure(2);
subplot(2,1,1);
hold on
for i=1:length(a)-1
    Mtemp = M;
    Ind = find(a(i)<= Mtemp(:,1) & Mtemp(:,1)<a(i+1));
    Mtemp= Mtemp(Ind,:);
    Num = size(Mtemp,1);
    Yaxis = 1:Num;
    c = CL(i,:);
%     scatter(Mtemp(:,2),Yaxis,[],c,'x');%,c,CL(:,i))
    histogram(Mtemp(:,2),10,'FaceColor',c)
end
legend('0<a<3.5','3.5<a<7','7<a<20','20<a');
xlabel('e');
ylabel('num');
%set(gca,'xscale','log')
hold off

subplot(2,1,2);
hold on
for i=1:length(a)-1
    Mtemp = M;
    Ind = find(a(i)<= Mtemp(:,1) & Mtemp(:,1)<a(i+1));
    Mtemp= Mtemp(Ind,:);
    Num = size(Mtemp,1);
    Mtemp = sortrows(Mtemp,2);
    c = CL(i,:);
    plot(Mtemp(:,2),((1:Num)/Num),'color',c)
end
%set(gca,'xscale','log')
legend('0<a<3.5','3.5<a<7','7<a<20','20<a');
xlabel('e');
ylabel('cdf');
saveas(figure(2),'e_distribution.jpg')
hold off

figure(3);
subplot(2,1,1);
hold on
for i=1:length(a)-1
    Mtemp = M;
    Ind = find(a(i)<= Mtemp(:,1) & Mtemp(:,1)<a(i+1));
    Mtemp= Mtemp(Ind,:);
    Num = size(Mtemp,1);
    Yaxis = 1:Num;
    c = CL(i,:);
    %     scatter(Mtemp(:,3),Yaxis,[],c,'x');%,c,CL(:,i))
    histogram(Mtemp(:,3),10,'FaceColor',c)
end
legend('0<a<3.5','3.5<a<7','7<a<20','20<a');
xlabel('inc[rad]');
ylabel('num');
%set(gca,'xscale','log')
hold off

subplot(2,1,2);
hold on
for i=1:length(a)-1
    Mtemp = M;
    Ind = find(a(i)<= Mtemp(:,1) & Mtemp(:,1)<a(i+1));
    Mtemp= Mtemp(Ind,:);
    Num = size(Mtemp,1);
    Mtemp = sortrows(Mtemp,3);
    c = CL(i,:);
    plot(Mtemp(:,3),((1:Num)/Num),'color',c)
end
legend('0<a<3.5','3.5<a<7','7<a<20','20<a');
xlabel('inc[rad]');
ylabel('cdf');
%set(gca,'xscale','log')

saveas(figure(3),'inc_distribution.jpg')
hold off
%%
a = [0,3.5,7,20,Inf];
%a = [0,Inf];
figure(5);
subplot(2,2,1);
hold on
for i=1:length(a)-1
    Mtemp = M;
    Ind = find(a(i)<= Mtemp(:,1) & Mtemp(:,1)<a(i+1));
    Mtemp= Mtemp(Ind,:);
    Num = size(Mtemp,1);
    Yaxis = 1:Num;
    c = CL(i,:);
    scatter(Mtemp(:,1),Mtemp(:,2),[],c,'x');%,c,CL(:,i))
%   [~,edges] = histcounts(log10(Mtemp(:,1)));
%    histogram(x,10.^edges)
%     plot(Mtemp(:,1),c)
end
%legend('gr1','gr2','gr3','gr4');
xlabel('a[AU]');
ylabel('e');
set(gca,'xscale','log')
hold off


subplot(2,2,2);
hold on
for i=1:length(a)-1
    Mtemp = M;
    Ind = find(a(i)<= Mtemp(:,1) & Mtemp(:,1)<a(i+1));
    Mtemp= Mtemp(Ind,:);
    Num = size(Mtemp,1);
    Yaxis = 1:Num;
    c = CL(i,:);
    scatter(Mtemp(:,1),Mtemp(:,3).*180/pi,[],c,'x');%,c,CL(:,i))
%   [~,edges] = histcounts(log10(Mtemp(:,1)));
%    histogram(x,10.^edges)
%     plot(Mtemp(:,1),c)
end
%legend('gr1','gr2','gr3','gr4');
xlabel('a[AU]');
ylabel('inc[deg]');
set(gca,'xscale','log')
hold off

subplot(2,2,3);
hold on
for i=1:length(a)-1
    Mtemp = M;
    Ind = find(a(i)<= Mtemp(:,1) & Mtemp(:,1)<a(i+1));
    Mtemp= Mtemp(Ind,:);
    Num = size(Mtemp,1);
    Yaxis = 1:Num;
    c = CL(i,:);
    scatter(Mtemp(:,2),Mtemp(:,3).*180/pi,[],c,'x');%,c,CL(:,i))
%   [~,edges] = histcounts(log10(Mtemp(:,1)));
%    histogram(x,10.^edges)
%     plot(Mtemp(:,1),c)
end
%legend('gr1','gr2','gr3','gr4');
xlabel('e');
ylabel('inc[deg]');
%set(gca,'xscale','log')
hold off

subplot(2,2,4);
hold on
for i=1:length(a)-1
    Mtemp = M;
    Ind = find(a(i)<= Mtemp(:,1) & Mtemp(:,1)<a(i+1));
    Mtemp= Mtemp(Ind,:);
    Num = size(Mtemp,1);
    Yaxis = 1:Num;
    c = CL(i,:);
    scatter(Mtemp(:,1),Mtemp(:,4),[],c,'x');%,c,CL(:,i))
%   [~,edges] = histcounts(log10(Mtemp(:,1)));
%    histogram(x,10.^edges)
%     plot(Mtemp(:,1),c)
end
%legend('gr1','gr2','gr3','gr4');
xlabel('a[AU]');
ylabel('pericenter[AU]');
set(gca,'xscale','log','yscale','log')

saveas(figure(5),'aei_p.jpg')
hold off