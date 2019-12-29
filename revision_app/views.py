from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Goods
from django.views.generic import CreateView, ListView
from django.core.paginator import Paginator
import xlwt
from django.http import HttpResponse
from django.utils.translation import gettext
from django.contrib.auth.decorators import login_required


class GoodCreateView(CreateView):
    model = Goods
    fields = ['name', 'quantity', "price"]
    success_url = ''


    def get_context_data(self, **kwargs):
        context = super(GoodCreateView, self).get_context_data(**kwargs)
        context['goods'] = Goods.objects.order_by('-id')[:5]
        return context


def end(request):

    paginator = Paginator(Goods.objects.all(), 15)
    page = request.GET.get('page')
    goods = paginator.get_page(page)
    return render(request, 'revision_app/end.html', {'goods': goods})


def about(request):
    return render(request, template_name="revision_app/about.html")


def download(request):
    # content-type of response
    response = HttpResponse(content_type='application/ms-excel')

    # decide file name
    response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.xls"'

    # creating workbook
    wb = xlwt.Workbook(encoding='utf-8')

    # adding sheet
    ws = FitSheetWrapper(wb.add_sheet("sheet1"))

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    # headers are bold
    font_style.font.bold = True

    # column header names, you can use your own headers here
    columns = ['Name', 'Quantity', 'Price', gettext('Total Price'), ]

    # write column headers in sheet
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, gettext(columns[col_num]), font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER

    # get your data, from database or from a text file...
    data = Goods.objects.all()
    for my_row in data:
        row_num = row_num + 1
        ws.write(row_num, 0, my_row.name, font_style, alignment.horz)
        ws.write(row_num, 1, my_row.quantity, font_style)
        ws.write(row_num, 2, my_row.price, font_style)
        ws.write(row_num, 3, my_row.total_price, font_style)



    wb.save(response)
    data.delete()
    return response


def delete(request):
    last = Goods.objects.last()
    if last:
        last.delete()
    return redirect('main')


class FitSheetWrapper(object):
    """Try to fit columns to max size of any entry.
    To use, wrap this around a worksheet returned from the
    workbook's add_sheet method, like follows:

        sheet = FitSheetWrapper(book.add_sheet(sheet_name))

    The worksheet interface remains the same: this is a drop-in wrapper
    for auto-sizing columns.
    """
    def __init__(self, sheet):
        self.sheet = sheet
        self.widths = dict()

    def write(self, r, c, label='', *args, **kwargs):
        self.sheet.write(r, c, label, *args, **kwargs)
        width = 3800
        if width > self.widths.get(c, 0):
            self.widths[c] = width
            self.sheet.col(c).width = width

    def __getattr__(self, attr):
        return getattr(self.sheet, attr)